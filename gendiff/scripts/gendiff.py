#!/usr/bin/env python

from gendiff.gendiff import generate_diff
from gendiff.cli import parse_args, print_to_console


def main():
    print_to_console(
        generate_diff(
            parse_args().first_file,
            parse_args().second_file,
            parse_args().format,
        )
    )


if __name__ == "__main__":
    main()
