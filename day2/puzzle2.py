def is_safe_report(report):
    is_increasing = True
    is_decreasing = True
    
    # Check if adjacent levels differ by between 1 and 3 (inclusive)
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
        if report[i] < report[i + 1]:
            is_decreasing = False
        elif report[i] > report[i + 1]:
            is_increasing = False
    
    return is_increasing or is_decreasing

def is_safe_with_one_removal(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe_report(new_report):
            return True
    return False

def read_input_file(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            reports.append(list(map(int, line.split())))
    return reports

def count_safe_reports(file_path):
    reports = read_input_file(file_path)
    safe_count = 0
    for report in reports:
        if is_safe_report(report) or is_safe_with_one_removal(report):
            safe_count += 1
    return safe_count

# File path (set the correct path to your input file)
file_path = r"F:\Advent of Code\day2\problem2.txt"

# Calculate and print the number of safe reports
safe_reports = count_safe_reports(file_path)
print("Number of safe reports:", safe_reports)
