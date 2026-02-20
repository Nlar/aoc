from utils.file_loader import load_day_data

full_data = True

day_data = load_day_data(full_data)


def get_direction(report) -> bool:
    direction = int(report[0] < report[1]) + int(report[1] < report[2]) + int(report[2] < report[3])
    if direction >= 2:
        return True
    if direction <= -2:
        return False

    # Likely an "unsafe" report, still complete edge case when the first element of the report can be removed
    return report[1] < report[len(report) - 1]


def safe_report(report: list, positive_direction: bool, i=1) -> int:
    while i < len(report):
        abs_diff = abs(report[i] - report[i - 1])
        if abs_diff > 3 or abs_diff < 1:
            return i
        # Positive Fail
        if positive_direction and report[i] < report[i - 1]:
            return i
        if not positive_direction and report[i] > report[i - 1]:
            return i

        i += 1

    return -1


def get_report_slice(report, index, modifier):
    index_location = index + modifier

    if index_location < 0 or index_location >= len(report):
        return []

    left_side = max(0, index_location - 1)
    right_side = min(index_location + 2, len(report))

    return report[left_side:index_location] + report[index_location + 1:right_side]


def part_1():
    safe = 0
    for report in day_data:
        total_diff = 0
        found_unsafe = False
        i = 1
        while i < len(report):
            abs_diff = abs(report[i] - report[i - 1])
            if abs_diff > 3 or abs_diff < 1:
                found_unsafe = True
                break
            total_diff += abs_diff
            i += 1
        if not found_unsafe:
            report_diff = abs(report[0] - report[len(report) - 1])
            safe += report_diff == total_diff

    return safe


def part_2():
    safe = 0
    for report in day_data:
        direction = get_direction(report)
        if (issue_index := safe_report(report, direction)) == -1:
            safe += 1
            continue

        report_slice_n1 = get_report_slice(report, issue_index, -1)
        report_slice_0 = get_report_slice(report, issue_index, 0)

        if safe_report(report_slice_n1, direction) == -1:
            if (safe_report(report, direction, issue_index + 1)) == -1:
                safe += 1
                continue

        if safe_report(report_slice_0, direction) == -1:
            if (safe_report(report, direction, issue_index + 2)) == -1:
                safe += 1
                continue

        if issue_index == len(report) - 1:
            safe += 1
            continue

    return safe


print(f"Safe: {part_1()}")
print(f"Safe: {part_2()}")
