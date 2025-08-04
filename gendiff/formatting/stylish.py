from functools import reduce

from gendiff.diff import get_children, get_name, get_status, get_value, is_flat
from gendiff.formatting.utils import BRACE_CLOSE, BRACE_OPEN, DEFAULT_GAP


def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def get_diff_txt(differences, gap=DEFAULT_GAP, gapper=' '):
    def display(acc, diff):
        if is_flat(diff):
            status = get_status(diff)
            name = get_name(diff)
            value = normalize_value(get_value(diff))
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


def format_stylish_to_print(differences):
    diff_txt = get_diff_txt(differences)
    return f'{BRACE_OPEN}\n{diff_txt}\n{BRACE_CLOSE}'
