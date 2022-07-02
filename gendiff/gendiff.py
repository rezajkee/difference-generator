from gendiff.parser import parse
from gendiff.make_diff import get_diff
from gendiff.formatter import format
import os.path


def generate_diff(file1path, file2path, format_name='stylish'):
    data1 = get_data(file1path)
    data2 = get_data(file2path)
    return format(format_name, get_diff(data1, data2))


def get_format(file_path):
    file_name, format_name = os.path.splitext(file_path)
    return format_name[1:]


def get_data(file_path):
    raw_data = open(file_path)
    parsed_data = parse(raw_data, get_format(file_path))
    return parsed_data
