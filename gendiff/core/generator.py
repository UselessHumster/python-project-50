from functools import reduce
from pathlib import Path

from gendiff.core.reader import get_file_data
from gendiff.core.utils import (CHANGE_STATUS, make_diff, normalize_data,
                                format_diff_to_print)


def get_difference(data1, data2):
    normalize_data1 = normalize_data(data1)
    normalize_data2 = normalize_data(data2)
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    def difference(acc, key):
        value1 = normalize_data1.get(key, None)
        value2 = normalize_data2.get(key, None)

        if value1 == value2:
            acc.append(make_diff(CHANGE_STATUS['no changes'], key, value1))
        elif value2 is None:
            acc.append(make_diff(CHANGE_STATUS['minus'], key, value1))
        elif value1 is None:
            acc.append(make_diff(CHANGE_STATUS['plus'], key, value2))
        else:
            acc.append(make_diff(CHANGE_STATUS['minus'], key, value1))
            acc.append(make_diff(CHANGE_STATUS['plus'], key, value2))
        return acc

    return list(reduce(difference, all_keys, []))


def generate_diff(file1_path: Path, file2_path: Path):
    data1 = get_file_data(file1_path)
    data2 = get_file_data(file2_path)
    differences = get_difference(data1, data2)
    return  format_diff_to_print(differences)
