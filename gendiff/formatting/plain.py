from functools import reduce

from gendiff.diff import (
    flatten,
    get_children,
    get_name,
    get_new_value,
    get_old_value,
    get_status,
    get_value,
    is_added,
    is_changed,
    is_flat,
    is_updated,
    mk_complex_diff,
    mk_updated_diff,
)
from gendiff.formatting.utils import PLAINT_TXT_STATUS as TXT_STATUS


def get_updates_values(old_diff, new_diff):
    if is_flat(old_diff):
        old_value = get_value(old_diff)
    else:
        old_value = []

    if is_flat(new_diff):
        new_value = get_value(new_diff)
    else:
        new_value = []

    return old_value, new_value


def normalize_diffs_for_plain(differences):
    def updated_to_one(acc: list, diff):
        if not acc:
            previous_diff_name = ''
            previous_diff = ''
        else:
            previous_diff = acc[-1]
            previous_diff_name = get_name(previous_diff)
        name = get_name(diff)
        if previous_diff_name == get_name(diff):
            acc.pop()
            old, new = get_updates_values(previous_diff, diff)
            acc.append(mk_updated_diff(name, old, new))
            return acc

        if is_flat(diff):
            acc.append(diff)
            return acc

        children = get_children(diff)
        new_children = normalize_diffs_for_plain(children)
        status = get_status(diff)
        acc.append(mk_complex_diff(name, new_children, status))
        return acc

    return list(reduce(updated_to_one, differences, []))


def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, list):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value)
    if value is None:
        return 'null'
    return f"'{value}'"


def generate_plain_changes(diff, name):
    status = get_status(diff)
    diff_txt = f"Property '{name}' was {TXT_STATUS[status]}"
    if is_updated(diff):
        old_value = normalize_value(get_old_value(diff))
        new_value = normalize_value(get_new_value(diff))
        return f"{diff_txt}. From {old_value} to {new_value}"
    if is_added(diff):
        if is_flat(diff):
            value = normalize_value(get_value(diff))
        else:
            value = normalize_value(get_children(diff))
        return f"{diff_txt} with value: {value}"
    return diff_txt


def get_diff_txt(differences, parent_name, separator):
    def display(acc, diff):
        name = f'{parent_name}{separator}{get_name(diff)}'
        if is_flat(diff) and (not is_changed(diff)):
            return acc
        if is_changed(diff):
            acc.append(generate_plain_changes(diff, name))
            return acc
        children = get_children(diff)
        acc.append(get_diff_txt(children, name, '.'))
        return acc

    return flatten(list(reduce(display, differences, [])))


def format_plain_to_print(differences):
    differences = normalize_diffs_for_plain(differences)
    return "\n".join(get_diff_txt(differences, '', ''))


if __name__ == '__main__':
    pass
