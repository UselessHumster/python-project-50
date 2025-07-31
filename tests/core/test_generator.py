from pathlib import Path

from gendiff import generate_diff

def get_test_data_path(filename):
    return Path(__file__).parent.parent / "test_data" / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_generate_diff():
    file1_path = get_test_data_path('file1.json')
    file2_path = get_test_data_path('file2.json')
    expected = read_file('result.txt')

    assert generate_diff(file1_path, file2_path) == expected