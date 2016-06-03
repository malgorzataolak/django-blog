import re
# Example 1 - Multiline
pattern = "cc"
example = "abcd\ncc\n abcd"
regexp = re.compile(pattern,re.MULTILINE)