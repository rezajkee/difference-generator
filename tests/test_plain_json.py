from gendiff import generate_diff

def read_text_file(path):
    with open(path, "r") as f:
        return f.read()


def test_generate():
    file1path = 'tests/fixtures/file1.json'
    file2path = 'tests/fixtures/file2.json'
    diff = generate_diff(file1path, file2path)
    result = read_text_file('tests/fixtures/result_plain_json.txt')
    assert diff == result