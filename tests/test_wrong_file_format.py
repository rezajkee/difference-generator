import pytest
from gendiff.parser import parse


@pytest.mark.asyncio
async def test_wrong_format():
    with pytest.raises(ValueError):
        parse(None, "not_json")