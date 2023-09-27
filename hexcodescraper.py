# used for grabbing lists of hex codes from sites instead of copying induvidual values

import re

webpage_text = """
PASTE HERE
"""

hex_code_pattern = r'#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})'

hex_codes = re.findall(hex_code_pattern, webpage_text)

for hex_code in hex_codes:
    print("#" + hex_code)
