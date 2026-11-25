# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/jajanb923-netizen/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/jajanb923-netizen/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

The funniest single-line resignation letter — written for the [make.fun bounty](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1).

## The entry

> Dear boss, I quit: after three years of writing "per my last email," I have decided to write my last email.

107 characters, one line. The hated office phrase turns back on itself: the setup *is* the
grievance, the punchline *is* the resignation — and the resignation itself is the last email.

## How it works

`main.py` (Python 3.13 standard library only, deterministic, no network) writes the chosen line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs) and self-checks the gate before writing: UTF-8 text, 1–140 characters, a single line, not only whitespace.

## Files

- `main.py` — the entrypoint; writes the resignation line and enforces the gate.
- `CANDIDATES.md` — the 10 candidate lines, scored against the judging criteria, with the critique that picked the winner.
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the wallet that owns this entry.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
