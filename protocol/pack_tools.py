"""Evidence-pack builder and commitment tools for the FOMC forecast pilot. DRAFT - not frozen.

build_pack() turns saved documents and a capture log into pack.md, manifest.json and pack.sha256.
commit_bundle() and verify_bundle() fingerprint a set of files with a secret salt. No model is involved.
"""
import hashlib
import json
import os
import secrets
from datetime import datetime, timezone

CLASS_ORDER = ["fomc", "speech", "testimony", "beige_book", "bls", "bea"]
MARKET_TERMS = ["futures", "priced in", "market-implied", "market participants", "odds", "overnight index swap"]


def _sha(data):
    """Hex sha256 of bytes."""
    return hashlib.sha256(data).hexdigest()


def _market_passages(text):
    """Count paragraphs (split on newlines) containing a market term, case-insensitively."""
    return sum(1 for p in text.split("\n") if p.strip() and any(t in p.lower() for t in MARKET_TERMS))


def _read_doc(capture_dir, entry):
    """Return (bytes, text) if the file exists and matches the log's sha256 and byte count and decodes, else (None, None)."""
    try:
        with open(os.path.join(capture_dir, entry["file"]), "rb") as f:
            data = f.read()
        if _sha(data) != entry["in_page_sha256"] or len(data) != entry["bytes"]:
            return None, None
        return data, data.decode("utf-8")
    except (OSError, UnicodeDecodeError):
        return None, None


def _diff(manifest, previous_manifest_path):
    """Compare included documents with a previous manifest; return (added, removed, revised) lists of urls."""
    with open(previous_manifest_path, encoding="utf-8") as f:
        prev = {d["url"]: d["sha256"] for d in json.load(f) if d["status"] == "included"}
    now = {d["url"]: d["sha256"] for d in manifest if d["status"] == "included"}
    return ([u for u in now if u not in prev], [u for u in prev if u not in now],
            [u for u in now if u in prev and now[u] != prev[u]])


def build_pack(capture_dir, out_dir, checkpoint_id, cutoff_utc, word_ceiling=None, previous_manifest_path=None):
    """Build pack.md, manifest.json, pack.sha256 (and pack_diff.md) in out_dir from a capture; return a summary dict."""
    with open(os.path.join(capture_dir, "capture_log.jsonl"), encoding="utf-8") as f:
        log = [json.loads(line) for line in f if line.strip()]
    docs = []
    for entry in log:
        data, text = _read_doc(capture_dir, entry)
        doc = dict(entry)
        doc.update(sha256=_sha(data) if data is not None else None, text=text, position=None,
                   status="included" if data is not None else "capture_failed",
                   words=len(text.split()) if text is not None else None,
                   market_passages=_market_passages(text) if text is not None else None)
        docs.append(doc)
    included = sorted((d for d in docs if d["status"] == "included"),
                      key=lambda d: (CLASS_ORDER.index(d["source_class"]), d["order"]))
    if word_ceiling is not None:
        speeches = sorted((d for d in included if d["source_class"] == "speech"), key=lambda d: -d["order"])
        while speeches and sum(d["words"] for d in included) > word_ceiling:
            oldest = speeches.pop(0)
            oldest["status"] = "dropped"
            included.remove(oldest)
    for i, d in enumerate(included, 1):
        d["position"] = i
    parts = ["# Evidence pack\ncheckpoint: %s\ncutoff_utc: %s\nincluded documents: %d\n\n" % (checkpoint_id, cutoff_utc, len(included))]
    for d in included:
        parts.append("==== DOCUMENT %d: %s | %s | %s | published: %s ====\n\n%s\n\n"
                     % (d["position"], d["title"], d["source_class"], d["url"], d["published"], d["text"]))
    pack = "".join(parts).encode("utf-8")
    fingerprint = _sha(pack)
    manifest = [{**{k: v for k, v in d.items() if k != "text"}, "extraction_version": "1"} for d in docs]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "pack.md"), "wb") as f:
        f.write(pack)
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    with open(os.path.join(out_dir, "pack.sha256"), "w", encoding="utf-8") as f:
        f.write(fingerprint + "\n")
    summary = {"included": len(included), "capture_failed": sum(d["status"] == "capture_failed" for d in docs),
               "dropped": sum(d["status"] == "dropped" for d in docs), "words": sum(d["words"] for d in included),
               "pack_sha256": fingerprint}
    if previous_manifest_path:
        added, removed, revised = _diff(manifest, previous_manifest_path)
        lines = ["# Pack diff", ""]
        for title, urls in (("Added", added), ("Dropped or removed", removed), ("Revised", revised)):
            lines += ["## " + title] + ["- " + u for u in urls] + (["(none)"] if not urls else []) + [""]
        with open(os.path.join(out_dir, "pack_diff.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        summary.update(added=len(added), removed=len(removed), revised=len(revised))
    return summary


def _bundle_hash(file_paths, salt):
    """Return (bundle sha256, {basename: file sha256}) for the files and salt."""
    hashes = {}
    for p in file_paths:
        name = os.path.basename(p)
        if name in hashes:
            raise ValueError("duplicate file name: " + name)
        with open(p, "rb") as f:
            hashes[name] = _sha(f.read())
    text = "\n".join(["%s:%s" % (n, hashes[n]) for n in sorted(hashes)] + ["salt:" + salt])
    return _sha(text.encode("utf-8")), hashes


def commit_bundle(file_paths, out_dir, checkpoint_id, salt=None):
    """Write commitment.json (public) and commitment_private.json (salt, file hashes); return the bundle fingerprint."""
    salt = salt if salt is not None else secrets.token_hex(16)
    fingerprint, hashes = _bundle_hash(file_paths, salt)
    os.makedirs(out_dir, exist_ok=True)
    public = {"checkpoint": checkpoint_id, "bundle_sha256": fingerprint, "files": len(hashes),
              "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    with open(os.path.join(out_dir, "commitment.json"), "w", encoding="utf-8") as f:
        json.dump(public, f, indent=2)
    with open(os.path.join(out_dir, "commitment_private.json"), "w", encoding="utf-8") as f:
        json.dump({"salt": salt, "files": hashes}, f, indent=2)
    return fingerprint


def verify_bundle(file_paths, salt, expected):
    """True if the files and salt reproduce the expected bundle fingerprint."""
    try:
        return _bundle_hash(file_paths, salt)[0] == expected
    except (OSError, ValueError):
        return False
