def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(file.readlines())


def write_to_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)


def main():
    file1_path = "text1.txt"
    file2_path = "file2.txt"


if __name__ == "__main__":
    main()
