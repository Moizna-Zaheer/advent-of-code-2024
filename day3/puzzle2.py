import re

# Load the puzzle input
with open("F:/Advent of Code/day3/problem3.txt") as f:
    data = f.read().strip()

# Regular expressions for identifying instructions
mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Initialize variables
mul_enabled = True  # mul instructions start enabled
result_sum = 0

# Split data into segments by each new instruction
segments = re.split(r"(?=mul|do|don't)", data)

for segment in segments:
    if re.match(do_pattern, segment):
        mul_enabled = True
    elif re.match(dont_pattern, segment):
        mul_enabled = False
    elif mul_enabled:
        match = re.match(mul_pattern, segment)
        if match:
            x, y = map(int, match.groups())
            result_sum += x * y

# Output the result
print(result_sum)
