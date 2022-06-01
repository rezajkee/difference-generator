#!/usr/bin/env python

from gendiff.parser import parse
from gendiff.make_diff import get_diff
from gendiff.formatter import format


def generate_diff(file1path, file2path, format_name='stylish'):
    data1 = get_data(file1path)
    data2 = get_data(file2path)
    return format(format_name, get_diff(data1, data2))


def get_format(file_path):
    format_name = file_path.split(".")[-1]
    return format_name


def get_data(file_path):
    raw_data = open(file_path)
    parsed_data = parse(raw_data, get_format(file_path))
    return parsed_data
