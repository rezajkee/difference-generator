#!/usr/bin/env python

from gendiff.parser import get_parsed_data
from gendiff.make_diff import get_diff
from gendiff.formatters.formatter import format


def generate_diff(file1path, file2path, format_name='stylish'):
    data1 = get_parsed_data(file1path)
    data2 = get_parsed_data(file2path)
    return format(format_name, get_diff(data1, data2))
