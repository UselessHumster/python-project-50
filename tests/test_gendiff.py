from gendiff import generate_diff
from tests.utils import get_test_data_path, read_file


def test_generate_flat_diff():
    file1_json = get_test_data_path('json/flat1.json')
    file2_json = get_test_data_path('json/flat2.json')

    file1_yaml = get_test_data_path('yaml/flat1.yaml')
    file2_yaml = get_test_data_path('yaml/flat2.yaml')
    expected = read_file('full_format/flat_result.txt')

    assert generate_diff(file1_json, file2_json) == expected
    assert generate_diff(file1_yaml, file2_yaml) == expected


def test_generate_complex_diff():
    file1_json = get_test_data_path('json/complex1.json')
    file2_json = get_test_data_path('json/complex2.json')
    expected = read_file('full_format/complex_result.txt')
    diff = generate_diff(file1_json, file2_json)
    assert diff == expected


def test_plain_format():
    file1_json = get_test_data_path('json/complex1.json')
    file2_json = get_test_data_path('json/complex2.json')
    expected = read_file('plain_format/complex_result.txt')
    diff = generate_diff(file1_json, file2_json, 'plain')
    print(diff)
    assert diff == expected