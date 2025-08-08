import json

from gendiff.diff import (
    Type,
    get_children,
    get_name,
    get_status,
    get_value,
    is_flat,
    mk_diff,
)


def prepare_differences_for_json(differences):
    def normalize_status_and_type(diff):
        name = get_name(diff)
        status = get_status(diff).name
        if is_flat(diff):
            value = get_value(diff)

            return mk_diff(name, value, Type.flat.name, status)

        children = get_children(diff)
        new_children = prepare_differences_for_json(children)
        return mk_diff(name, new_children, Type.complex.name, status)

    return list(map(normalize_status_and_type, differences))


def format_json_to_print(differences: list):
    diffs = prepare_differences_for_json(differences)
    return json.dumps(diffs, indent=2)
