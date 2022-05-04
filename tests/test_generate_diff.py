from gendiff import generate_diff


def read_text_file(path):
    with open(path, "r") as f:
        return f.read()


def test_plain_json():
    file1path = 'tests/fixtures/file1.json'
    file2path = 'tests/fixtures/file2.json'
    diff = generate_diff(file1path, file2path)
    result = read_text_file('tests/fixtures/result_plain_json.txt')
    assert diff == result


def test_plain_json_plain():
    file1path = 'tests/fixtures/file1.json'
    file2path = 'tests/fixtures/file2.json'
    diff = generate_diff(file1path, file2path, 'plain')
    result = read_text_file('tests/fixtures/result_plain_json_plain.txt')
    assert diff == result


def test_plain_json_json():
    file1path = 'tests/fixtures/file1.json'
    file2path = 'tests/fixtures/file2.json'
    diff = generate_diff(file1path, file2path, 'json')
    result = read_text_file('tests/fixtures/result_plain_json_json.txt')
    assert diff == result


def test_plain_yaml():
    file1path = 'tests/fixtures/file1.yaml'
    file2path = 'tests/fixtures/file2.yaml'
    diff = generate_diff(file1path, file2path)
    result = read_text_file('tests/fixtures/result_plain_yaml.txt')
    assert diff == result


def test_nested_json():
    file1path = 'tests/fixtures/nested_file1.json'
    file2path = 'tests/fixtures/nested_file2.json'
    diff = generate_diff(file1path, file2path)
    result = read_text_file('tests/fixtures/result_nested_json.txt')
    assert diff == result


def test_nested_json_plain_format():
    file1path = 'tests/fixtures/nested_file1.json'
    file2path = 'tests/fixtures/nested_file2.json'
    diff = generate_diff(file1path, file2path, 'plain')
    result = read_text_file('tests/fixtures/result_plain_format.txt')
    assert diff == result


def test_nested_json_json_format():
    file1path = 'tests/fixtures/nested_file1.json'
    file2path = 'tests/fixtures/nested_file2.json'
    diff = generate_diff(file1path, file2path, 'json')
    result = read_text_file('tests/fixtures/result_json_format.txt')
    assert diff == result


def test_nested_yaml():
    file1path = 'tests/fixtures/nested_file1.yaml'
    file2path = 'tests/fixtures/nested_file2.yaml'
    diff = generate_diff(file1path, file2path)
    result = read_text_file('tests/fixtures/result_nested_yaml.txt')
    assert diff == result
