#!/usr/bin/env python

from gendiff.parser import parse
from gendiff.make_diff import get_diff
from gendiff.formatters.formatter import format


def generate_diff(file1path, file2path, formatter='stylish'):
    file1 = parse(file1path)
    file2 = parse(file2path)
    return format(formatter, get_diff(file1, file2))
