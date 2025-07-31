from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent.parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff():
    file1_json = get_test_data_path('file1.json')
    file2_json = get_test_data_path('file2.json')

    file1_yaml = get_test_data_path('file1.yaml')
    file2_yaml = get_test_data_path('file2.yaml')
    expected = read_file('result.txt')

    assert generate_diff(file1_json, file2_json) == expected
    assert generate_diff(file1_yaml, file2_yaml) == expected