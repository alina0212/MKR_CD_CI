import pytest
import os
from main import compare_files, read_file, write_to_file


@pytest.fixture
def create_test_files():
    file1_path = "test_file1.txt"
    file2_path = "test_file2.txt"
    with open(file1_path, 'w') as file1:
        file1.write("line1\nline2\nline3\n")
    with open(file2_path, 'w') as file2:
        file2.write("line2\nline3\nline4\n")
    yield file1_path, file2_path
    os.remove(file1_path)
    os.remove(file2_path)


def test_compare_files(create_test_files):
    file1_path, file2_path = create_test_files
    same_lines, diff_lines = compare_files(file1_path, file2_path)
    assert same_lines == {"line2\n", "line3\n"}
    assert diff_lines == {"line1\n", "line4\n"}


@pytest.fixture
def create_test_file():
    file_path = "test_file.txt"
    with open(file_path, 'w') as file:
        file.write("line1\nline2\nline3\n")
    yield file_path
    os.remove(file_path)

