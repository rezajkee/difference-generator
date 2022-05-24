import pytest
from gendiff import generate_diff


@pytest.mark.asyncio
async def test_wrong_format(file1_yml_path, file2_yml_path):
    with pytest.raises(ValueError):
        generate_diff(file1_yml_path, file2_yml_path, "something")
