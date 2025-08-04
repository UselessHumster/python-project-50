from pathlib import Path

from gendiff.diff import mktree
from gendiff.formatting import (
    format_json_to_print,
    format_plain_to_print,
    format_stylish_to_print,
)
from gendiff.parser import get_difference, parse_data
from gendiff.reader import get_file_data


def generate_diff(file1_path: Path, file2_path: Path, _format='stylish'):
    tree1 = mktree(parse_data(get_file_data(file1_path)))
    tree2 = mktree(parse_data(get_file_data(file2_path)))
    differences = get_difference(tree1, tree2)
    if _format == 'plain':
        return format_plain_to_print(differences)
    if _format == 'json':
        return format_json_to_print(differences)
    return format_stylish_to_print(differences)






