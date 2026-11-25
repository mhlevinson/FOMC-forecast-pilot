# Protocol freeze - v6, 25 Nov 2026

The protocol of the FOMC forecast pilot is frozen as of the commit that adds this version of this file. Rule S1 (`design.md`, section B): no scored forecast before the freeze is public and witnessed; a later change creates a new version and a new cohort.

- **Version:** v6 (design v3 of 22 Nov 2026 with `amendments.md` rows 1-30 folded in).
- **Replaces:** v5, frozen 25 Nov 2026 in commit `2737f547c8bc74d3e715355f754cf8fb2aed0bbe` (combined fingerprint `d538f456cfe71be16aaae434f52e61af425dcee93ae3a8ccbde4527e2804756c`; archived at https://web.archive.org/web/20261125135150/https://api.github.com/repos/mhlevinson/FOMC-forecast-pilot/commits/2737f547c8bc74d3e715355f754cf8fb2aed0bbe), and v4, frozen 24 Nov 2026 in commit `1a435ea0c34a15873abed5cc78ca5c24de161127`. No forecast was made under v4 or v5. The only change from v5 is row 30: the archive witness captures the commit's GitHub API record, because the archive receives a 404 for github.com commit pages. Protocol files other than `design.md`, `run_sheet.md` and `amendments.md` change only in their header line.
- **Frozen by:** the lab's principal, Michael Levinson, through the runner session of 25 Nov 2026.
- **Forecasts existing at the freeze:** unscored only - the dress rehearsal R (23 Nov) and two dry runs (24 Nov). No scored forecast.
- **Tests:** `test_forecast_tools.py`, `test_pack_tools.py` and `test_venue_tools.py` all pass on these files.
- **Witness:** this repository's server-side push time, and a web-archive capture of this commit's GitHub API record, recorded in the commit that follows it (the capture cannot be inside the file it captures).
- **Agent type:** `.claude/agents/pilot-forecaster.md` is a copy of the definition in the `fomc-pilot` plugin (v0.1.0) installed on the principal's account; preflight step 3(b) checks the installed type has only Read and Write.

## Fingerprints (sha256)

Check from the repository root with `sha256sum -c` on the block below.

```
fe48933419902d225eaa539653870b55d2535af03b4091a8704f5fdb115678e4  protocol/amendments.md
e89cc52144eecb3593e22ef551554ac52f962ac01d587499b69b1ef7de970ce8  protocol/design.md
a081367c92cdac0473a401a9cb49f7c91229d179e68c96a72385356f334f0e1f  protocol/forecast_tools.py
f1685dddcb1371b1bfe9cd83b12f3647b2bef2726fb93ad4157fda1704ce8222  protocol/pack_tools.py
707145f4e95e7bfead85eb78f4edc441f87dd7e883a0b9375b27b7d3b76861a9  protocol/prompts.md
492c4e9031e11627ed4f897d4c4d6695b3f1c296a7c84a750ca5b91cf2eba805  protocol/questions.md
0e34162e89092c3cbb22d3ccf37ada7d777a207cc080b80c70e5a48b15af5221  protocol/run_sheet.md
889dc03785f632deca095618d1752d91c6de397cb0a60f5cbdff280a3276028d  protocol/sources.md
b149d2a2a047e504f40f5144985071cd2684f42884bcc031d542ee34baf3b4ca  protocol/test_forecast_tools.py
caaace2396970ead68a833f9b6f43105cef92f762973187af1bb6e0118b8f649  protocol/test_pack_tools.py
ed677a748d3f6569341e8f52222c178822ba0949869969b42a75d9a9dc3ca169  protocol/test_venue_tools.py
b823b3ae2b1174c99c36dc94643abd47e3f073ebc1d73f3b936dbac3c836ee44  protocol/venue_tools.py
b71751dc16dc61222ebbea24b90a5a75856bfb606d2ad89a0680fbc9283293ba  protocol/venues.md
3a0484169495e6fe8d2b4913cef277e9e992d2110b386db46229b7716a8908fc  .claude/agents/pilot-forecaster.md
```

**Combined fingerprint** (sha256 of the block above as a text file, one line per file, ending in a newline):

`4b0fe75b8e7f257238cb3bfb2bff91ecbca401a7b0aba3909a63a651febc51ab`
