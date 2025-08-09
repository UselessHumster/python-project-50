from functools import reduce

from gendiff.diff import (
    Status,
    Type,
    get_children,
    get_children_names,
    get_diff_by_name,
    get_name,
    get_type,
    get_value,
    is_complex,
    is_flat,
    mk_diff,
)


def parse_data(data):
    sorted_data = dict(sorted(data.items()))

    def normalizer(val):
        key = val[0]
        value = val[1]
        if isinstance(value, dict):
            return mk_diff(key, parse_data(value), _type=Type.complex)
        return mk_diff(key, value, _type=Type.flat)
    return list(map(normalizer, sorted_data.items()))


def get_difference(tree1, tree2):
    all_names = sorted(set(get_children_names(tree1)) |
                       set(get_children_names(tree2)))

    def collect_diffs(acc, name):
        child1 = get_diff_by_name(name, get_children(tree1))
        child2 = get_diff_by_name(name, get_children(tree2))

        if not all((is_complex(child1), is_complex(child2))):
            return _compare_diffs(child1, child2, acc, name)

        children = get_difference(child1, child2)
        name = get_name(child1)
        acc.append(mk_diff(name, children, Type.complex))
        return acc

    return reduce(collect_diffs, all_names, [])


def _has_difference(child1, child2):
    if not child1:
        return False
    if not child2:
        return False
    if get_value(child1) != get_value(child2):
        return False
    return True


def _has_been_removed(child1, child2):
    if not child1:
        return False
    if child2 and (get_value(child1) == get_value(child2)):
        return False
    return True


def _has_been_added(child1, child2):
    if child1 and child2 and (get_value(child1) == get_value(child2)):
        return False
    if not child2:
        return False
    return True


def _compare_to_flat(child1, child2, acc):
    if _has_difference(child1, child2):
        acc.append(child1)
    if _has_been_removed(child1, child2):
        name = get_name(child1)
        value = get_value(child1)
        acc.append(mk_diff(name, value, Type.flat, Status.removed))
    if _has_been_added(child1, child2):
        name = get_name(child2)
        value = get_value(child2)
        acc.append(mk_diff(name, value, Type.flat, Status.added))
    return acc


def _compare_none_to_other(child1, child2, acc, name, status, child_to_check):
    match get_type(child_to_check):
        case Type.flat:
            return _compare_to_flat(child1, child2, acc)
        case Type.complex:
            children = get_children(child_to_check)
            acc.append(mk_diff(name, children, Type.complex, status))
            return acc


def _compare_flat_to_complex(child1, child2, acc, name, is_flat_removed):
    value = get_value(child1)
    children = get_children(child2)
    flat_status = Status.removed if is_flat_removed else Status.added
    complex_status = Status.added if is_flat_removed else Status.removed
    changes = [mk_diff(name, value, Type.flat, flat_status),
               mk_diff(name, children, Type.complex, complex_status)]

    return (acc + changes) if is_flat_removed else (acc + changes[::-1])


def _compare_diffs(child1, child2, acc, name):
    if child1 is None:
        return _compare_none_to_other(
            child1, child2, acc, name, Status.added, child_to_check=child2)

    if child2 is None:
        return _compare_none_to_other(
            child1, child2, acc, name, Status.removed, child_to_check=child1)

    if is_flat(child1) and is_flat(child2):
        return _compare_to_flat(child1, child2, acc)

    if is_flat(child1):
        return _compare_flat_to_complex(
            child1, child2, acc, name, is_flat_removed=True)

    if is_flat(child2):
        return _compare_flat_to_complex(
            child2, child1, acc, name, is_flat_removed=False)
