import json
from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


FLAT1_JSON = get_test_data_path('data/flat1.json')
FLAT2_JSON = get_test_data_path('data/flat2.json')

FLAT1_YAML = get_test_data_path('data/flat1.yaml')
FLAT2_YAML = get_test_data_path('data/flat2.yaml')

COMPLEX1_JSON = get_test_data_path('data/complex1.json')
COMPLEX2_JSON = get_test_data_path('data/complex2.json')

FLAT_STYLISH_RESULT = read_file('results/stylish_flat.txt')
COMPLEX_STYLISH_RESULT = read_file('results/stylish_complex.txt')
COMPLEX_PLAIN_RESULT = read_file('results/plain_complex.txt')
COMPLEX_JSON_RESULT = read_file('results/json_complex.txt')

flat_parsed_path = get_test_data_path('parsed_data/flat.json')
PARSED_DATA_FLAT = json.load(open(flat_parsed_path))

complex_parsed_path = get_test_data_path('parsed_data/complex.json')
PARSED_DATA_COMPLEX = json.load(open(complex_parsed_path))