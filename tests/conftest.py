import os
import pytest
import asyncio
import pytest_asyncio

FIXTURES_FOLDER = 'fixtures'


@pytest.fixture(scope='module')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def file1_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'file1.json')


@pytest.fixture(scope='session')
def file2_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'file2.json')


@pytest.fixture(scope='session')
def nested_file1_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'nested_file1.json')


@pytest.fixture(scope='session')
def nested_file2_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'nested_file2.json')


@pytest.fixture(scope='session')
def file1_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'file1.yaml')


@pytest.fixture(scope='session')
def file2_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'file2.yaml')


@pytest.fixture(scope='session')
def nested_file1_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'nested_file1.yaml')


@pytest.fixture(scope='session')
def nested_file2_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'nested_file2.yaml')


@pytest_asyncio.fixture(scope='function')
async def result_render(request):
    assert getattr(request.module, 'FORMATTER', None)

    result_path = os.path.join(
        os.path.dirname(__file__), FIXTURES_FOLDER, request.module.FORMATTER)

    with open(result_path) as file:
        return file.read()
