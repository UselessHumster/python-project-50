from gendiff.diff import mktree
from gendiff.parser import get_difference, parse_data
from gendiff.reader import get_file_data
from tests.utils import (
    COMPLEX1_JSON,
    COMPLEX2_JSON,
    FLAT1_JSON,
    FLAT2_JSON,
    PARSED_DATA_COMPLEX,
    PARSED_DATA_FLAT,
)


def test_get_difference():
    tree1 = mktree(parse_data(get_file_data(FLAT1_JSON)))
    tree2 = mktree(parse_data(get_file_data(FLAT2_JSON)))

    result = get_difference(tree1, tree2)
    assert result == PARSED_DATA_FLAT

    tree1 = mktree(parse_data(get_file_data(COMPLEX1_JSON)))
    tree2 = mktree(parse_data(get_file_data(COMPLEX2_JSON)))

    result = get_difference(tree1, tree2)
    assert result == PARSED_DATA_COMPLEX
