import json
from pathlib import Path

import yaml


def get_file_data(file: Path) -> dict | None:
    try:
        data = load_file(file)
    except Exception as e:
        print(e)
        return None
    return data


def load_file(file):
    if file.suffix == '.json':
        return get_data_from_json(file)
    elif file.suffix == '.yaml' or file.suffix == '.yml':
        return get_data_from_yaml(file)
    else:
        raise Exception(f"Can't parse '{file.suffix}' files")


def get_data_from_json(file):
    return json.load(open(file))


def get_data_from_yaml(file):
    return yaml.safe_load(open(file))