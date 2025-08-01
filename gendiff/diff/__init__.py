def mktree(children):
    return mk_complex_diff('/', children)


def mk_flat_diff(name, value, change_status=' '):
    return {'name': name,
            'value': value,
            'status': change_status,
            'type': 'flat'
            }


def mk_complex_diff(name, children, change_status=' '):
    return {'name': name,
            'children': children,
            'status': change_status,
            'type': 'complex'
            }


def get_status(diff):
    return diff['status']


def get_name(diff):
    return diff['name']


def get_value(diff):
    return diff['value']


def get_children(diff):
    return diff['children']


def is_flat(diff):
    return diff['type'] == 'flat'


def is_complex(diff):
    return diff['type'] == 'complex'


def get_diff_by_name(name, children):
    for child in children:
        if get_name(child) == name:
            return child
    return None


def get_children_names(diff: dict):
    return list(map(lambda child: get_name(child), get_children(diff)))


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
