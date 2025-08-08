import argparse


def create_parser():
    parser = argparse.ArgumentParser(prog='gendiff')
    parser.add_argument('-f', '--format', help='set format of output',
                        choices=['stylish', 'plain', 'json'])
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser
