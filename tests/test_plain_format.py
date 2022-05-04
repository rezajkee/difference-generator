from pydoc import plain
from test_plain_json import read_text_file
from gendiff import generate_diff


def test_generate():
    file1path = 'tests/fixtures/nested_file1.json'
    file2path = 'tests/fixtures/nested_file2.json'
    diff = generate_diff(file1path, file2path, 'plain')
    result = read_text_file('tests/fixtures/result_plain_format.txt')
    assert diff == result