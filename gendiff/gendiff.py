#!/usr/bin/env python

from gendiff.parser import parse
from gendiff.make_diff import get_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def generate_diff(file1path, file2path, formatter='stylish'):
    formatters = {
        'stylish': stylish,
        'plain': plain,
    }
    file1 = parse(file1path)
    file2 = parse(file2path)
    return formatters[formatter](get_diff(file1, file2))
