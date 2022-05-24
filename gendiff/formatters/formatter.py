from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jsonf


def format(format_name, tree):
    formatters = {
        "stylish": stylish,
        "plain": plain,
        "json": jsonf,
    }
    if format_name in formatters:
        return formatters[format_name](tree)
    else:
        raise ValueError(
            '"{}" format not found. Try "stylish", "plain" or "json".'.format(
                format_name
            )
        )
