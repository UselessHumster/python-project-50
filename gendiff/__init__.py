from functools import reduce
from pathlib import Path

from gendiff.diff import (
    get_children,
    get_name,
    get_status,
    get_value,
    is_flat,
    mktree,
)
from gendiff.parser import get_difference, parse_data
from gendiff.reader import get_file_data

DEFAULT_GAP = 2
BRACE_OPEN = '{'
BRACE_CLOSE = '}'


def generate_diff(file1_path: Path, file2_path: Path):
    tree1 = mktree(parse_data(get_file_data(file1_path)))
    tree2 = mktree(parse_data(get_file_data(file2_path)))
    differences = get_difference(tree1, tree2)
    return format_diff_to_print(differences)


def get_diff_txt(differences, gap=DEFAULT_GAP, gapper=' '):
    def display(acc, diff):
        if is_flat(diff):
            status = get_status(diff)
            name = get_name(diff)
            value = get_value(diff)
            acc.append(f"{gapper * gap}{status} {name}: {value}")
            return acc
        status = get_status(diff)
        name = get_name(diff)
        children = get_children(diff)
        acc.append(f"{gapper * gap}{status} {name}: {BRACE_OPEN}\n"
                   f"{get_diff_txt(children, gap + 4)}\n"
                   f"{gapper * gap}  {BRACE_CLOSE}")
        return acc

    return "\n".join(list(reduce(display, differences, [])))


def format_diff_to_print(differences):
    diff_txt = get_diff_txt(differences)
    return f'{BRACE_OPEN}\n{diff_txt}\n{BRACE_CLOSE}'
