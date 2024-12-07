with open(r"F:\Advent of Code\day2\problem2.txt") as f:
    data = f.read().strip().split("\n")

def is_safe(report):
    levels = list(map(int, report.split()))
    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]

    # Check if all differences are between -3 and 3 (inclusive) but not zero
    if any(abs(diff) > 3 or diff == 0 for diff in differences):
        return False

    # Check if all differences are consistently increasing or decreasing
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True

    return False

# Count the number of safe reports
safe_count = sum(1 for report in data if is_safe(report))
print(safe_count)
