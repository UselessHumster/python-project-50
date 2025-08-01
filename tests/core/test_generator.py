from gendiff import generate_diff
from tests.utils import get_test_data_path, read_file


def test_generate_flat_diff():
    file1_json = get_test_data_path('file1.json')
    file2_json = get_test_data_path('file2.json')

    file1_yaml = get_test_data_path('file1.yaml')
    file2_yaml = get_test_data_path('file2.yaml')
    expected = read_file('result.txt')
    diff = generate_diff(file1_json, file2_json)
    print(f'{diff=}')
    assert generate_diff(file1_json, file2_json) == expected
    assert generate_diff(file1_yaml, file2_yaml) == expected


def test_generate_complex_diff():
    file3_json = get_test_data_path('file3.json')
    file4_json = get_test_data_path('file4.json')
    expected = read_file('result2.txt')
    diff = generate_diff(file3_json, file4_json)
    assert diff == expected