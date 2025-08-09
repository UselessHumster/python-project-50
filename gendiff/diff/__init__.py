from enum import Enum


class Status(Enum):
    not_changed = ' '
    updated = '+-'
    added = '+'
    removed = '-'


class Type(Enum):
    flat = 'flat'
    complex = 'complex'
    updated = 'updated'


def mk_diff(name, value, _type: Type | str, status=Status.not_changed):
    match _type:
        case Type.flat | Type.flat.name:
            return {'name': name,
                    'value': value,
                    'status': status,
                    'type': _type
                    }
        case Type.complex | Type.complex.name:
            return {'name': name,
                    'children': value,
                    'status': status,
                    'type': _type
                    }
        case Type.updated | Type.updated.name:
            old_value, new_value = value[0], value[1]
            return {'name': name,
                    'from': old_value,
                    'to': new_value,
                    'status': Status.updated,
                    'type': _type
                    }
        case _:
            raise Exception(f'Unknown type {_type}')


def mktree(children):
    return mk_diff('/', children, _type=Type.complex)


def get_old_value(updated_diff):
    return updated_diff['from']


def get_new_value(updated_diff):
    return updated_diff['to']


def get_status(diff) -> Status:
    return diff['status']


def get_type(diff) -> Type:
    return diff['type']


def get_name(diff):
    return diff['name']


def get_value(flat_diff):
    return flat_diff['value']


def get_children(complex_diff):
    return complex_diff['children']


def get_diff_by_name(name, children):
    for child in children:
        if get_name(child) == name:
            return child
    return None


def get_children_names(diff: dict):
    return [get_name(child) for child in get_children(diff)]


def is_changed(diff):
    return get_status(diff) != Status.not_changed


def is_flat(diff):
    return diff['type'] == Type.flat


def is_complex(diff):
    if diff is None:
        return False
    return diff['type'] == Type.complex


def is_updated(diff):
    return diff['type'] == Type.updated


def is_removed(diff):
    return get_status(diff) == Status.removed


def is_added(diff):
    return get_status(diff) == Status.added


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:

            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(tree)

    return result
