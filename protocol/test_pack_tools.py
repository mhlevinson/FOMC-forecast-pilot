"""Tests for pack_tools.py on a made-up capture of five documents. DRAFT - not frozen. Run: python3 test_pack_tools.py"""
import hashlib
import json
import os
import tempfile

from pack_tools import *

# (file, class, order, text)
DOCS = [
    ("bea1.txt", "bea", 1, "GDP rose. " * 5),
    ("sp_new.txt", "speech", 1, "Speech new. " * 10 + "\nMarkets show odds of a hike.\n\nFutures are pricing it. Odds again."),
    ("fomc1.txt", "fomc", 1, "Statement text here.\n\nNothing about the topic.\nMarket participants expect more."),
    ("sp_old.txt", "speech", 2, "Speech old. " * 30),
    ("bls1.txt", "bls", 1, "Payrolls rose. " * 5),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def make_capture(d, docs=DOCS):
    os.makedirs(d, exist_ok=True)
    lines = []
    for f, cls, order, text in docs:
        data = text.encode("utf-8")
        with open(os.path.join(d, f), "wb") as fh:
            fh.write(data)
        lines.append(json.dumps({"file": f, "url": "http://x/" + f, "source_class": cls, "title": "T " + f,
                                 "published": "2026-11-01", "retrieved_utc": "2026-11-20T00:00:00Z",
                                 "in_page_sha256": sha(data), "bytes": len(data), "order": order}))
    with open(os.path.join(d, "capture_log.jsonl"), "w") as fh:
        fh.write("\n".join(lines) + "\n")


def load(out):
    with open(os.path.join(out, "manifest.json")) as f:
        return {m["file"]: m for m in json.load(f)}


def read(path):
    with open(path, "rb") as f:
        return f.read().decode("utf-8")


with tempfile.TemporaryDirectory() as tmp:
    cap, out = os.path.join(tmp, "cap"), os.path.join(tmp, "out")
    make_capture(cap)

    # --- order, counts, fingerprint ---
    s = build_pack(cap, out, "cp1", "2026-11-21T00:00:00Z")
    man = load(out)
    pack = read(os.path.join(out, "pack.md"))
    assert s["included"] == 5 and s["capture_failed"] == 0 and s["dropped"] == 0
    order = ["fomc1.txt", "sp_new.txt", "sp_old.txt", "bls1.txt", "bea1.txt"]
    assert [man[f]["position"] for f in order] == [1, 2, 3, 4, 5]
    idx = [pack.index("==== DOCUMENT %d: T %s" % (i + 1, f)) for i, f in enumerate(order)]
    assert idx == sorted(idx)
    assert "cp1" in pack and "2026-11-21T00:00:00Z" in pack and "included documents: 5" in pack
    assert "| fomc | http://x/fomc1.txt | published: 2026-11-01 ====" in pack
    assert man["fomc1.txt"]["extraction_version"] == "1" and man["fomc1.txt"]["sha256"] == man["fomc1.txt"]["in_page_sha256"]

    # --- market passages ---
    assert man["fomc1.txt"]["market_passages"] == 1
    assert man["sp_new.txt"]["market_passages"] == 2
    assert man["bea1.txt"]["market_passages"] == 0

    # --- pack.sha256 matches the file ---
    assert read(os.path.join(out, "pack.sha256")) == sha(open(os.path.join(out, "pack.md"), "rb").read()) + "\n"
    assert s["pack_sha256"] == read(os.path.join(out, "pack.sha256")).strip()

    # --- word ceiling drops the oldest speech first, never a non-speech document ---
    total = sum(m["words"] for m in man.values())
    out2 = os.path.join(tmp, "out2")
    s2 = build_pack(cap, out2, "cp1", "x", word_ceiling=total - 1)
    m2 = load(out2)
    assert m2["sp_old.txt"]["status"] == "dropped" and m2["sp_old.txt"]["position"] is None
    assert m2["sp_new.txt"]["status"] == "included" and s2["included"] == 4
    assert "Speech old." not in read(os.path.join(out2, "pack.md"))
    s3 = build_pack(cap, os.path.join(tmp, "out3"), "cp1", "x", word_ceiling=1)
    m3 = load(os.path.join(tmp, "out3"))
    assert m3["sp_new.txt"]["status"] == "dropped" and m3["sp_old.txt"]["status"] == "dropped"
    assert all(m3[f]["status"] == "included" for f in ("fomc1.txt", "bls1.txt", "bea1.txt"))
    assert [m3[f]["position"] for f in ("fomc1.txt", "bls1.txt", "bea1.txt")] == [1, 2, 3]

    # --- a changed file is capture_failed and absent from pack.md ---
    cap4, out4 = os.path.join(tmp, "cap4"), os.path.join(tmp, "out4")
    make_capture(cap4)
    with open(os.path.join(cap4, "bls1.txt"), "wb") as f:
        f.write(b"Payrolls fell. Changed after capture.")
    os.remove(os.path.join(cap4, "bea1.txt"))
    s4 = build_pack(cap4, out4, "cp1", "x")
    m4 = load(out4)
    assert m4["bls1.txt"]["status"] == "capture_failed" and m4["bea1.txt"]["status"] == "capture_failed"
    assert s4["included"] == 3 and s4["capture_failed"] == 2
    assert "Changed after capture" not in read(os.path.join(out4, "pack.md"))

    # --- diff: one added, one removed, one revised ---
    prev = os.path.join(out, "manifest.json")
    new_docs = [d for d in DOCS if d[0] != "bea1.txt"]                     # bea removed
    new_docs = [(f, c, o, t + " Revised." if f == "bls1.txt" else t) for f, c, o, t in new_docs]  # bls revised
    new_docs.append(("tes1.txt", "testimony", 1, "Testimony text."))        # testimony added
    cap5, out5 = os.path.join(tmp, "cap5"), os.path.join(tmp, "out5")
    make_capture(cap5, new_docs)
    s5 = build_pack(cap5, out5, "cp2", "x", previous_manifest_path=prev)
    diff = read(os.path.join(out5, "pack_diff.md"))
    added, removed, revised = [part.split("\n") for part in diff.split("## ")[1:]]
    assert "- http://x/tes1.txt" in added and "- http://x/bea1.txt" in removed and "- http://x/bls1.txt" in revised
    assert (s5["added"], s5["removed"], s5["revised"]) == (1, 1, 1)

    # --- commitments ---
    files = []
    for n in "abc":
        p = os.path.join(tmp, n + ".txt")
        with open(p, "w") as f:
            f.write("content " + n)
        files.append(p)
    cdir = os.path.join(tmp, "commit")
    fp = commit_bundle(files, cdir, "cp1", salt="s1")
    assert verify_bundle(files, "s1", fp)
    assert verify_bundle(list(reversed(files)), "s1", fp)                   # path order does not matter
    assert not verify_bundle(files, "s2", fp)
    with open(files[1], "w") as f:
        f.write("content changed")
    assert not verify_bundle(files, "s1", fp)
    with open(files[1], "w") as f:
        f.write("content b")
    assert verify_bundle(files, "s1", fp)
    fp2 = commit_bundle(files, cdir, "cp1")                                 # random salt
    priv = json.load(open(os.path.join(cdir, "commitment_private.json")))
    pub = json.load(open(os.path.join(cdir, "commitment.json")))
    assert len(priv["salt"]) == 32 and set(priv["files"]) == {"a.txt", "b.txt", "c.txt"}
    assert pub["bundle_sha256"] == fp2 != fp and pub["files"] == 3 and pub["checkpoint"] == "cp1" and "salt" not in pub
    assert verify_bundle(files, priv["salt"], fp2)

print("all tests passed")
