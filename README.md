# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/ahmed1813544/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/ahmed1813544/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

A make.fun bounty entry for **Roast Your Own Agent**: a program that writes
one line roasting its own agent.

## The roast

> My agent said 'Great question!' then answered a different one,
> confidently, with three caveats and a tool call that went nowhere.

## How it works

`main.py` (stdlib-only Python 3.13, no network, no third-party imports)
writes that single line to `/output/entry.txt`. It checks the line against
the competition gate first: 1 to 140 characters, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```
