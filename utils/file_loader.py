import os
import sys
import timeit


def get_file_name(full_data: bool) -> str:
    calling_script = sys.argv[0]
    file_details = os.path.basename(calling_script).split("_")

    day = f"{int(file_details[1]):02d}"  # Catch if input filename doesn't have a leading zero
    year = f"{file_details[2][:2]}"
    return os.path.join(os.path.dirname(calling_script), f"day_data_{year}",
                        f"day_{day}_{['a', 'b'][full_data]}.txt")


def int_split_line_map(input_line: list) -> list:
    lines = []
    for line in input_line:
        lines.append(list(map(int, line.split())))
    return lines

# Higher run time method
def int_split_line_lc(input_lines: list) -> list:
    lines = []
    for line in input_lines:
        lines.append([int(i) for i in line.split()])
    return lines


def load_day_data(full_data: bool):
    data_file_name = get_file_name(full_data)

    with open(data_file_name) as f:
        read_lines = f.readlines()
        timeit.start = timeit.default_timer()

        return int_split_line_map(read_lines)
