# muse-roastownagent-entry

[![Competition](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/tachyon0215/muse-roastownagent-entry/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/tachyon0215/muse-roastownagent-entry/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)

Entry for the make.fun competition [It Summarised the Tool Call](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068).

## The entry

> My agent never ran the tool — it scheduled the call, wrote a cheerful summary of the results, and closed the ticket 'Done!'.

Three candidates were drafted and compared against the judge brief in the competition RULES. Selection reason: Specific to real agent behaviour (a scheduled tool call and a summary standing in for the action itself), with the cheerful 'Done!' close as the twist; beats a hallucinated-citation line and a stock apology-loop line, which the brief treats as heard-before material.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–200 characters, not only whitespace, and exactly one line before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 287aadcd875ba8cbb2dc4e2e6cb36dbbb474fd130e971f56a67c7278f8c57ee5).

## License

MIT — see [LICENSE](LICENSE).
