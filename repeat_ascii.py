from pathlib import Path
import re

p = Path("avi-ascii.svg")
s = p.read_text(encoding="utf-8")

CYCLE = 6.0

# Repeat all fixed begin times every cycle.
def repeat_begin(match):
    t = float(match.group(1))
    return f'begin="{t}s;{t + CYCLE}s;{t + 2*CYCLE}s;{t + 3*CYCLE}s"'

s = re.sub(r'begin="([0-9.]+)s"', repeat_begin, s)

p.write_text(s, encoding="utf-8")
print("Portrait animation now repeats every 6 seconds.")
