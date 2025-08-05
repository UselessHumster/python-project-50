def mktree(children):
    return mk_complex_diff('/', children)


def mk_flat_diff(name, value, change_status='not_changed'):
    return {'name': name,
            'value': value,
            'status': change_status,
            'type': 'flat'
            }


def mk_complex_diff(name, children, change_status='not_changed'):
    return {'name': name,
            'children': children,
            'status': change_status,
            'type': 'complex'
            }


def mk_updated_diff(name, old_value, new_value):
    return {'name': name,
            'from': old_value,
            'to': new_value,
            'status': 'updated',
            'type': 'updated'
            }


def get_old_value(updated_diff):
    return updated_diff['from']


def get_new_value(updated_diff):
    return updated_diff['to']


def get_status(diff):
    return diff['status']


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
    return [get_name(child) for child in diff]


def is_changed(diff):
    return get_status(diff) != 'not_changed'


def is_flat(diff):
    return diff['type'] == 'flat'


def is_complex(diff):
    return diff['type'] == 'complex'


def is_updated(diff):
    return diff['type'] == 'updated'


def is_removed(diff):
    return get_status(diff) == 'removed'


def is_added(diff):
    return get_status(diff) == 'added'


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
