from functools import reduce

from gendiff.diff import get_children, get_name, get_status, get_value, is_flat
from gendiff.formatting.utils import BRACE_CLOSE, BRACE_OPEN, GAP, GAP_COUNT


def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def get_diff_txt(differences, gap_count=GAP_COUNT, gap=GAP):
    def display(acc, diff):
        status = get_status(diff).value
        name = get_name(diff)
        if is_flat(diff):
            value = normalize_value(get_value(diff))
            acc.append(f"{gap * gap_count}{status} {name}: {value}")
            return acc

        children = get_children(diff)
        acc.append(f"{gap * gap_count}{status} {name}: {BRACE_OPEN}\n"
                   f"{get_diff_txt(children, gap_count + 4)}\n"
                   f"{gap * gap_count}  {BRACE_CLOSE}")
        return acc

    return "\n".join(reduce(display, differences, []))


def format_stylish_to_print(differences):
    diff_txt = get_diff_txt(differences)
    return f'{BRACE_OPEN}\n{diff_txt}\n{BRACE_CLOSE}'
