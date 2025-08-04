from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


FLAT1_JSON = get_test_data_path('json/flat1.json')
FLAT2_JSON = get_test_data_path('json/flat2.json')

FLAT1_YAML = get_test_data_path('yaml/flat1.yaml')
FLAT2_YAML = get_test_data_path('yaml/flat2.yaml')

COMPLEX1_JSON = get_test_data_path('json/complex1.json')
COMPLEX2_JSON = get_test_data_path('json/complex2.json')

FLAT_STYLISH_RESULT = read_file('full_format/flat_result.txt')
COMPLEX_STYLISH_RESULT = read_file('full_format/complex_result.txt')
COMPLEX_PLAIN_RESULT = read_file('plain_format/complex_result.txt')
COMPLEX_JSON_RESULT = read_file('json_format/complex_result.txt')