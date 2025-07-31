CHANGE_STATUS = {'minus' : '-',
                 'no changes': ' ',
                 'plus': '+'}

def make_diff(status, key, value):
    return {'status': status,
            'key': key,
            'value': value}


def get_status(diff):
    return diff['status']


def get_diff_key(diff):
    return diff['key']


def get_diff_value(diff):
    return diff['value']


def normalize_data(data):
    sorted_data = dict(sorted(data.items()))
    return dict(
        list(map(
            lambda x: (x[0], str(x[1]).lower()),
            sorted_data.items())
        )
    )


def format_diff_to_print(differences):
    diff_txt = "\n  ".join(
        [(f"{get_status(diff)} "
          f"{get_diff_key(diff)}: "
          f"{get_diff_value(diff)}")
         for diff in differences])

    return ('{\n'
            f'  {diff_txt}\n'
            '}')