import json

import pytest

from gendiff import generate_diff
from tests.utils import (
    COMPLEX1_JSON,
    COMPLEX2_JSON,
    COMPLEX_JSON_RESULT,
    COMPLEX_PLAIN_RESULT,
    COMPLEX_STYLISH_RESULT,
    FLAT1_JSON,
    FLAT1_YAML,
    FLAT2_JSON,
    FLAT2_YAML,
    FLAT_STYLISH_RESULT,
)


def test_generate_diff():
    result = generate_diff(FLAT1_JSON, FLAT2_JSON)
    assert result == FLAT_STYLISH_RESULT

    result = generate_diff(FLAT1_YAML, FLAT2_YAML)
    assert result == FLAT_STYLISH_RESULT

    result = generate_diff(COMPLEX1_JSON, COMPLEX2_JSON)
    assert result == COMPLEX_STYLISH_RESULT

    result = generate_diff(COMPLEX1_JSON, COMPLEX2_JSON, 'plain')
    assert result == COMPLEX_PLAIN_RESULT

    result = generate_diff(COMPLEX1_JSON, COMPLEX2_JSON, 'json')
    assert result == COMPLEX_JSON_RESULT

    try:
        json.loads(result)
    except Exception as e:
        msg = ('json diff is not a valid json string, '
               'got error: "{}", got diff: {}').format(e, result)
        pytest.fail(msg)