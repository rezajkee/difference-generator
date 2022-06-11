from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def format(format_name, tree):
    formatters = {
        "stylish": render_stylish,
        "plain": render_plain,
        "json": render_json,
    }
    if format_name in formatters:
        return formatters[format_name](tree)
    raise ValueError(
        f'"{format_name}" format not found. Try "stylish", "plain" or "json".'
    )
