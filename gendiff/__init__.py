from pathlib import Path

from gendiff.diff import mktree
from gendiff.formatting import (
    format_json_to_print,
    format_plain_to_print,
    format_stylish_to_print,
)
from gendiff.parser import get_difference, parse_data
from gendiff.reader import get_file_data


def generate_diff(file1_path, file2_path, _format='stylish'):
    file1 = Path(file1_path)
    file2 = Path(file2_path)
    tree1 = mktree(parse_data(get_file_data(file1)))
    tree2 = mktree(parse_data(get_file_data(file2)))
    differences = get_difference(tree1, tree2)
    if _format == 'plain':
        return format_plain_to_print(differences)
    if _format == 'json':
        return format_json_to_print(differences)
    return format_stylish_to_print(differences)






