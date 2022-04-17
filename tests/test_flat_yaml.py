from test_flat_json import read_text_file
from gendiff import generate_diff


def test_generate():
    file1path = 'tests/fixtures/file1.yaml'
    file2path = 'tests/fixtures/file2.yaml'
    diff = generate_diff(file1path, file2path)
    result = read_text_file('tests/fixtures/result_flat_yaml.txt')
    assert diff == result