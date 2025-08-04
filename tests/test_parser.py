from gendiff.diff import mktree
from gendiff.parser import get_difference, parse_data
from gendiff.reader import get_file_data
from tests.utils import get_test_data_path


def test_parse_data():
    file1_json = get_test_data_path('json/flat3.json')
    parsed = parse_data(get_file_data(file1_json))
    expected = [
        {'name': 'follow', 'value': False, 'status': ' ', 'type': 'flat'},
        {'name': 'host', 'value': 'hexlet.io', 'status': ' ', 'type': 'flat'},
        {
            'name': 'proxy',
            'value': '123.234.53.22',
            'status': ' ',
            'type': 'flat'},
        {'name': 'test', 'value': None, 'status': ' ', 'type': 'flat'},
        {'name': 'timeout', 'value': 50, 'status': ' ', 'type': 'flat'}

    ]
    print(parsed)
    assert parsed == expected


def test_get_difference():
    file1_json = get_test_data_path('json/flat1.json')
    file2_json = get_test_data_path('json/flat2.json')
    tree1 = mktree(parse_data(get_file_data(file1_json)))
    tree2 = mktree(parse_data(get_file_data(file2_json)))

    expected = [
        {'name': 'follow', 'value': False, 'status': '-', 'type': 'flat'},
        {'name': 'host', 'value': 'hexlet.io', 'status': ' ', 'type': 'flat'},
        {
            'name': 'proxy',
            'value': '123.234.53.22',
            'status': '-',
            'type': 'flat'},
        {'name': 'timeout', 'value': 50, 'status': '-', 'type': 'flat'},
        {'name': 'timeout', 'value': 20, 'status': '+', 'type': 'flat'},
        {'name': 'verbose', 'value': True, 'status': '+', 'type': 'flat'}]

    result = get_difference(tree1, tree2)
    assert result == expected

    file1_json = get_test_data_path('json/complex1.json')
    file2_json = get_test_data_path('json/complex2.json')
    tree1 = mktree(parse_data(get_file_data(file1_json)))
    tree2 = mktree(parse_data(get_file_data(file2_json)))
    expected = [
        {'name': 'common', 'children':
            [{'name': 'follow', 'value': False, 'status': '+', 'type': 'flat'},
             {
                 'name': 'setting1',
                 'value': 'Value 1',
                 'status': ' ',
                 'type': 'flat'},
             {'name': 'setting2', 'value': 200, 'status': '-', 'type': 'flat'},
             {'name': 'setting3', 'value': True, 'status': '-', 'type': 'flat'},
             {'name': 'setting3', 'value': None, 'status': '+', 'type': 'flat'},
             {
                 'name': 'setting4',
                 'value': 'blah blah',
                 'status': '+',
                 'type': 'flat'},
             {'name': 'setting5', 'children':
                 [{
                     'name': 'key5',
                     'value': 'value5',
                     'status': ' ',
                     'type': 'flat'}],
              'status': '+', 'type': 'complex'},
             {'name': 'setting6', 'children':
                 [{'name': 'doge', 'children':
                     [{
                         'name': 'wow',
                         'value': '',
                         'status': '-',
                         'type': 'flat'},
                      {
                          'name': 'wow',
                          'value': 'so much',
                          'status': '+',
                          'type': 'flat'}],
                   'status': ' ', 'type': 'complex'},
                  {'name': 'key',
                   'value': 'value',
                   'status': ' ',
                   'type': 'flat'},
                  {
                      'name': 'ops',
                      'value': 'vops',
                      'status': '+',
                      'type': 'flat'}],
              'status': ' ', 'type': 'complex'}],
         'status': ' ', 'type': 'complex'},
        {'name': 'group1', 'children':
            [{'name': 'baz', 'value': 'bas', 'status': '-', 'type': 'flat'},
             {'name': 'baz', 'value': 'bars', 'status': '+', 'type': 'flat'},
             {'name': 'foo', 'value': 'bar', 'status': ' ', 'type': 'flat'},
             {'name': 'nest', 'children':
                 [{
                     'name': 'key',
                     'value': 'value',
                     'status': ' ',
                     'type': 'flat'}],
              'status': '-', 'type': 'complex'},
             {'name': 'nest', 'value': 'str', 'status': '+', 'type': 'flat'}],
         'status': ' ', 'type': 'complex'},
        {'name': 'group2', 'children':
            [{
                'name': 'abc',
                'value': 12345,
                'status': ' ',
                'type': 'flat'},
             {'name': 'deep', 'children':
                 [{'name': 'id', 'value': 45, 'status': ' ', 'type': 'flat'}],
              'status': ' ', 'type': 'complex'}],
         'status': '-', 'type': 'complex'},
        {'name': 'group3', 'children':
            [{'name': 'deep', 'children':
                [{'name': 'id', 'children':
                    [{
                        'name': 'number',
                        'value': 45,
                        'status': ' ',
                        'type': 'flat'}],
                  'status': ' ', 'type': 'complex'}],
              'status': ' ', 'type': 'complex'},
             {'name': 'fee', 'value': 100500, 'status': ' ', 'type': 'flat'}],
         'status': '+', 'type': 'complex'}]

    result = get_difference(tree1, tree2)
    print(result)
    assert result == expected
