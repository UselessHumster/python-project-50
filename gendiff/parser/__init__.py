from functools import reduce

from gendiff.diff import (
    get_children,
    get_children_names,
    get_diff_by_name,
    get_name,
    get_value,
    is_complex,
    is_flat,
    mk_complex_diff,
    mk_flat_diff,
)


def parse_data(data):
    sorted_data = dict(sorted(data.items()))

    def normalizer(val):
        key = val[0]
        value = val[1]

        if isinstance(value, dict):
            return mk_complex_diff(key, parse_data(value))

        return mk_flat_diff(key, value)
    return list(map(normalizer, sorted_data.items()))


def not_changed_child(child1, child2):
    if not child1:
        return False
    if not child2:
        return False
    if get_value(child1) != get_value(child2):
        return False
    return True


def removed_child(child1, child2):
    if not child1:
        return False
    if child2:
        if get_value(child1) == get_value(child2):
            return False
    return True


def added_child(child1, child2):
    if child1:
        if child2:
            if get_value(child1) == get_value(child2):
                return False
    if not child2:
        return False
    return True


def check_simple_diff(child1, child2, acc):
    if not_changed_child(child1, child2):
        acc.append(child1)
    if removed_child(child1, child2):
        name = get_name(child1)
        value = get_value(child1)
        acc.append(mk_flat_diff(name, value, '-'))
    if added_child(child1, child2):
        name = get_name(child2)
        value = get_value(child2)
        acc.append(mk_flat_diff(name, value, '+'))
    return acc


def get_difference(tree1, tree2):
    all_names = sorted(set(get_children_names(tree1)) |
                       set(get_children_names(tree2)))

    def collect_diffs(acc, name):
        child1 = get_diff_by_name(name, get_children(tree1))
        child2 = get_diff_by_name(name, get_children(tree2))

        if child1 is None:
            if is_flat(child2):
                return check_simple_diff(child1, child2, acc)
            children = get_children(child2)
            acc.append(mk_complex_diff(name, children, '+'))
            return acc

        if child2 is None:
            if is_flat(child1):
                return check_simple_diff(child1, child2, acc)
            children = get_children(child1)
            acc.append(mk_complex_diff(name, children, '-'))
            return acc

        if is_flat(child1) and is_flat(child2):
            return check_simple_diff(child1, child2, acc)

        if is_flat(child1) and is_complex(child2):
            value = get_value(child1)
            children = get_children(child2)
            acc.append(mk_flat_diff(name, value, '-'))
            acc.append(mk_complex_diff(name, children, '+'))
            return acc

        if is_flat(child2) and is_complex(child1):
            value = get_value(child2)
            children = get_children(child1)
            acc.append(mk_complex_diff(name, children, '-'))
            acc.append(mk_flat_diff(name, value, '+'))
            return acc

        children = get_difference(child1, child2)
        name = get_name(child1)
        acc.append(mk_complex_diff(name, children, ' '))
        return acc

    return list(reduce(collect_diffs, all_names, []))
