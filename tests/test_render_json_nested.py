import pytest
from gendiff import generate_diff

FIXTURE_NAME = 'json_nested'


@pytest.mark.asyncio
async def test_json(
    nested_file1_json_path, nested_file2_json_path, result_render
):
    assert result_render == generate_diff(
        nested_file1_json_path, nested_file2_json_path, 'json'
    )


@pytest.mark.asyncio
async def test_yml(nested_file1_yml_path, nested_file2_yml_path, result_render):
    assert result_render == generate_diff(
        nested_file1_yml_path, nested_file2_yml_path, 'json'
    )
