# Protocol freeze - v4, 24 Nov 2026

The protocol of the FOMC forecast pilot is frozen as of the commit that adds this file. Rule S1 (`design.md`, section B): no scored forecast before the freeze is public and witnessed; a later change creates a new version and a new cohort.

- **Version:** v4 (design v3 of 22 Nov 2026 with `amendments.md` rows 1-28 folded in).
- **Frozen by:** the lab's principal, Michael Levinson, through the runner session of 24 Nov 2026.
- **Forecasts existing at the freeze:** unscored only - the dress rehearsal R (23 Nov) and two dry runs (24 Nov). No scored forecast.
- **Tests:** `test_forecast_tools.py`, `test_pack_tools.py` and `test_venue_tools.py` all pass on these files.
- **Witness:** this repository's server-side push time, and a web-archive capture of this commit, recorded in the commit that follows it (the capture cannot be inside the file it captures).
- **Agent type:** `.claude/agents/pilot-forecaster.md` is a copy of the definition in the `fomc-pilot` plugin (v0.1.0) installed on the principal's account; preflight step 3(b) checks the installed type has only Read and Write.

## Fingerprints (sha256)

Check from the repository root with `sha256sum -c` on the block below.

```
3754a74499917d49249db8f48da47ee8241b2c1b2fc295801760b8f02f302fe5  protocol/amendments.md
67a3226ec5efe034a093a708fec2f97a73d1a993e2c755523cd2a4f4ea6fb2a2  protocol/design.md
a081367c92cdac0473a401a9cb49f7c91229d179e68c96a72385356f334f0e1f  protocol/forecast_tools.py
f1685dddcb1371b1bfe9cd83b12f3647b2bef2726fb93ad4157fda1704ce8222  protocol/pack_tools.py
1ca4825dc8447692c332ed9f3ea11f120fad536b817ea77626b130ab25930385  protocol/prompts.md
62524df47e564000b82950beb87ae66e1e7303e547b8aeffcf4404d6141b4228  protocol/questions.md
65635afca87fd5c7682c1b57efafc17f7fb582207c6be0daa1fcd2c1c3268320  protocol/run_sheet.md
eb059432f1d849d1e1cb79027cb22743337ba536c7c2f4fb73f9ffea10e1d903  protocol/sources.md
b149d2a2a047e504f40f5144985071cd2684f42884bcc031d542ee34baf3b4ca  protocol/test_forecast_tools.py
caaace2396970ead68a833f9b6f43105cef92f762973187af1bb6e0118b8f649  protocol/test_pack_tools.py
ed677a748d3f6569341e8f52222c178822ba0949869969b42a75d9a9dc3ca169  protocol/test_venue_tools.py
b823b3ae2b1174c99c36dc94643abd47e3f073ebc1d73f3b936dbac3c836ee44  protocol/venue_tools.py
79b4e7667a8cc068dec2de129e6f7d24c3c1de38329cd46c4dd8fc8cb20c49d5  protocol/venues.md
3a0484169495e6fe8d2b4913cef277e9e992d2110b386db46229b7716a8908fc  .claude/agents/pilot-forecaster.md
```

**Combined fingerprint** (sha256 of the block above as a text file, one line per file, ending in a newline):

`b67396182c9cf1b03a98cd84b99dd12cc68adf36f82476adcf5c922c5ad9cd34`
