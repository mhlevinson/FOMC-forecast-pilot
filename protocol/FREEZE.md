# Protocol freeze - v5, 25 Nov 2026

The protocol of the FOMC forecast pilot is frozen as of the commit that adds this version of this file. Rule S1 (`design.md`, section B): no scored forecast before the freeze is public and witnessed; a later change creates a new version and a new cohort.

- **Version:** v5 (design v3 of 22 Nov 2026 with `amendments.md` rows 1-29 folded in).
- **Replaces:** v4, frozen 24 Nov 2026 in commit `1a435ea0c34a15873abed5cc78ca5c24de161127` (combined fingerprint `b67396182c9cf1b03a98cd84b99dd12cc68adf36f82476adcf5c922c5ad9cd34`). No forecast was made under v4. The only change is row 29: the twin run is restored at K1-K4, J1, J2 and J6, and with it the anchor check.
- **Frozen by:** the lab's principal, Michael Levinson, through the runner session of 25 Nov 2026.
- **Forecasts existing at the freeze:** unscored only - the dress rehearsal R (23 Nov) and two dry runs (24 Nov). No scored forecast.
- **Tests:** `test_forecast_tools.py`, `test_pack_tools.py` and `test_venue_tools.py` all pass on these files.
- **Witness:** this repository's server-side push time, and a web-archive capture of this commit, recorded in the commit that follows it (the capture cannot be inside the file it captures).
- **Agent type:** `.claude/agents/pilot-forecaster.md` is a copy of the definition in the `fomc-pilot` plugin (v0.1.0) installed on the principal's account; preflight step 3(b) checks the installed type has only Read and Write.

## Fingerprints (sha256)

Check from the repository root with `sha256sum -c` on the block below.

```
6bc3b3f148da5a1eea0142f3e35f2c061c8a18a5ac481fdd78eac04b2d412fb6  protocol/amendments.md
910871908bf05777274cf01e1087bc10ac7754192fbabd64f2afee0122942d4e  protocol/design.md
a081367c92cdac0473a401a9cb49f7c91229d179e68c96a72385356f334f0e1f  protocol/forecast_tools.py
f1685dddcb1371b1bfe9cd83b12f3647b2bef2726fb93ad4157fda1704ce8222  protocol/pack_tools.py
50b9eb8eae2862de8eb067434db4f5f05e388d73f5795aecd5c1bd97baed6aaf  protocol/prompts.md
6ea434af48ed5d662be0a88b272ef98a3f0b4b1f251e52c75f1271165e9a21e8  protocol/questions.md
795d83570e4278a3728b6aec506eeceaa4e8124bca46897663526b391dc3e34a  protocol/run_sheet.md
04e8b72f9d7e21380b840dd01852cd6e3b68d35a09f7adc0d94db35ad05098d1  protocol/sources.md
b149d2a2a047e504f40f5144985071cd2684f42884bcc031d542ee34baf3b4ca  protocol/test_forecast_tools.py
caaace2396970ead68a833f9b6f43105cef92f762973187af1bb6e0118b8f649  protocol/test_pack_tools.py
ed677a748d3f6569341e8f52222c178822ba0949869969b42a75d9a9dc3ca169  protocol/test_venue_tools.py
b823b3ae2b1174c99c36dc94643abd47e3f073ebc1d73f3b936dbac3c836ee44  protocol/venue_tools.py
6d0bf93f6e5426dbf52bc973796a52cebc7679e6d86a03759fc196ec1b2fb476  protocol/venues.md
3a0484169495e6fe8d2b4913cef277e9e992d2110b386db46229b7716a8908fc  .claude/agents/pilot-forecaster.md
```

**Combined fingerprint** (sha256 of the block above as a text file, one line per file, ending in a newline):

`d538f456cfe71be16aaae434f52e61af425dcee93ae3a8ccbde4527e2804756c`
