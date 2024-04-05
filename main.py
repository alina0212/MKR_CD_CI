import os
from typing import Set


def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(file.readlines())


def write_to_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(list(lines))  # Convert set to list


def compare_files(file1_path, file2_path) -> tuple[Set[str], Set[str]]:
    """

    :param file1_path:
    :param file2_path:
    :return:
    """
    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)

    # Find common lines
    same_lines = set()
    for line in file1_lines:
        if line in file2_lines:
            same_lines.add(line)

    # Find lines that are different (present in only one file)
    diff_lines = set()
    for line in file1_lines:
        if line not in file2_lines:
            diff_lines.add(line)

    for line in file2_lines:
        if line not in file1_lines:
            diff_lines.add(line)

    return same_lines, diff_lines


def main():
    file1_path = os.path.join("text1.txt")
    file2_path = os.path.join("text2.txt")
    same_lines, diff_lines = compare_files(file1_path, file2_path)

    write_to_file("same.txt", same_lines)
    write_to_file("diff.txt", diff_lines)


if __name__ == "__main__":
    main()
