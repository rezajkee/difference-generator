import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output (stylish by default)'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    return parser.parse_args()
