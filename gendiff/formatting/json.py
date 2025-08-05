import json


def format_json_to_print(differences: list):
    return json.dumps(differences, indent=2)
