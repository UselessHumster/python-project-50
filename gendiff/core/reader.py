import json


def get_file_data(file) -> dict | None:
    try:
        data = json.load(open(file))
    except Exception as e:
        print(e)
        return None
    return data
