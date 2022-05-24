INDENTS = {
    "same": "  ",
    "added": "+ ",
    "removed": "- "
}


def stylish(source, depth=1):
    children = source.get("children")
    indent = build_indent(depth)
    formatted_value = stringify(source.get("value"), depth)
    formatted_value1 = stringify(source.get("value1"), depth)
    formatted_value2 = stringify(source.get("value2"), depth)

    if source["type"] == "root":
        lines = map(stylish, children)
        result = "\n".join(lines)
        return "{{\n{}\n}}".format(result)

    if source["type"] == "nested":
        lines = map(lambda child: stylish(child, depth + 1), children)
        result = "\n".join(lines)
        return "{0}  {1}: {{\n{2}\n{3}  }}".format(
            indent,
            source["key"],
            result,
            indent
        )

    if source["type"] == "modified":
        old_val = "{0}- {1}: {2}".format(
            indent,
            source["key"],
            formatted_value1
        )
        new_val = "{0}+ {1}: {2}".format(
            indent,
            source["key"],
            formatted_value2
        )
        return "{0}\n{1}".format(old_val, new_val)

    if source["type"] in INDENTS:
        type_of_indent = INDENTS[source["type"]]
        return "{0}{1}{2}: {3}".format(
            indent, type_of_indent, source["key"], formatted_value
        )


def build_indent(depth):
    return ' ' * (depth * 4 - 2)


def stringify(value, depth=1):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return "null"
    if isinstance(value, dict):
        result = ['{',
                  '{0}  {1}'.format(build_indent(depth), '}')]

        for key, val in value.items():
            indent = build_indent(depth + 1)
            result.insert(-1, '{0}  {1}: {2}'.format(
                indent, key, stringify(val, depth + 1)
            ))
        return '\n'.join(result)
    return value
