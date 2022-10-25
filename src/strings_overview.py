import re

one_line_str = 'some string'
multiline_str = """
multiline string, line 1
line 2"""

print(one_line_str)
print(f"Substring (2, end): {one_line_str[2:]}")
print(f"Substring (1, 4): {one_line_str[1:4]}")
print(f'Is l in {one_line_str}? : {"l" in one_line_str}')
print(f'Is s in {one_line_str}? : {"s" in one_line_str}')
print()

another_str = "some different text"
print(f'Index of k in {another_str}: {another_str.find("k")}')
print(f'Index of d in {another_str}: {another_str.find("d")}')
print(f'Replace white spaces with 2 in {another_str}: {another_str.replace(" ", "1")}')
print(f"To uppercase: {another_str.upper()}")
print(f"TO LOWER CASE: {'TO_LOWER_CASE'.lower()}")
print()

to_strip_str = "  with too many white spaces \t"
print(f"Stripped |{to_strip_str}|: |{to_strip_str.strip()}|")

to_split_str = "a | b | c | yet another character"
print(f"To split str: {to_split_str}, split: {to_split_str.split('|')}")

yet_another_string = "yet another string"
print(f"{yet_another_string} starts with 'yet'? {yet_another_string.startswith('yet')}")
print(f"{yet_another_string} starts with 'et'? {yet_another_string.startswith('et')}")
print(f"{yet_another_string} ends with 'ing'? {yet_another_string.endswith('ing')}")
print(f"{yet_another_string} ends with 'in'? {yet_another_string.endswith('in')}")
print()

regex_str = 'a|sth|z'
regex = re.compile('^a(.*)z$')
r_match = regex.match(regex_str)
print(f'{regex_str} matches regex({regex.pattern}): {r_match.group(1)}')
