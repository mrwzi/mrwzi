from pathlib import Path
import re

p = Path("avi-ascii.svg")
s = p.read_text(encoding="utf-8")

# Improve only the original green cursor rectangles
s = re.sub(
    r'width="6\.0" height="10\.0" fill="#39d353" opacity="0"',
    'width="10.0" height="11.0" fill="#69f0a0" opacity="0"',
    s
)

# Make cursor a little softer
s = s.replace('<set attributeName="opacity" to="0.9"', '<set attributeName="opacity" to="0.75"')

# Slow only the moving cursor animation a bit
s = re.sub(
    r'(<animate attributeName="x"[^>]*dur=")0\.34s(")',
    r'\g<1>0.45s\2',
    s
)

p.write_text(s, encoding="utf-8")
print("updated avi-ascii.svg")
