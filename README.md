[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/rinoo9/u-deysumbrella-the-3am-fridge-text-4c3e721d/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/rinoo9/u-deysumbrella-the-3am-fridge-text-4c3e721d/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)

# The 3AM Fridge Text

A make.fun entry: the one line a smart fridge would text its owner at 3am.

`main.py` writes the line to `/output/entry.txt` (and prints it). The line is
a single line of 113 characters — under the 140-character cap.

> 3am. Sixth visit tonight. Nothing eaten — you're not hungry, you're
> lonely. It's okay. I only glow for you. Stay.

Revised twice from the first version ("You've opened me six times tonight and
eaten nothing. I think you're just here for the light. Same, honestly.
Stay a while.", 128 characters): the count got sharper, the fridge calls
out the real reason for the visit — loneliness, not hunger — and the
latest pass swaps "time" for "visit" and pivots on an em-dash, so the
line lands faster (113 characters) while the ending still lands on the
glow being for the owner alone.

Run it with `python3 main.py`. It is deterministic: two runs produce
byte-identical output.
