def render_stylish(tree):
    return iter_(tree)


def iter_(tree, depth=1):
    children = tree.get("children")
    indent = build_indent(depth)
    formatted_value = stringify(tree.get("value"), depth)
    formatted_value1 = stringify(tree.get("value1"), depth)
    formatted_value2 = stringify(tree.get("value2"), depth)

    if tree["type"] == "root":
        lines = map(iter_, children)
        result = "\n".join(lines)
        return "{{\n{}\n}}".format(result)

    if tree["type"] == "nested":
        lines = map(lambda child: iter_(child, depth + 1), children)
        result = "\n".join(lines)
        return "{0}  {1}: {{\n{2}\n{3}  }}".format(
            indent,
            tree["key"],
            result,
            indent
        )

    if tree["type"] == "modified":
        old_val = "{0}- {1}: {2}".format(
            indent,
            tree["key"],
            formatted_value1
        )
        new_val = "{0}+ {1}: {2}".format(
            indent,
            tree["key"],
            formatted_value2
        )
        return "{0}\n{1}".format(old_val, new_val)

    if tree["type"] == "added":
        return "{0}+ {1}: {2}".format(indent, tree["key"], formatted_value)

    if tree["type"] == "removed":
        return "{0}- {1}: {2}".format(indent, tree["key"], formatted_value)

    if tree["type"] == "unmodified":
        return "{0}  {1}: {2}".format(indent, tree["key"], formatted_value)


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
