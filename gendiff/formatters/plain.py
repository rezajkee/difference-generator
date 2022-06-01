def render_plain(tree):
    return iter_(tree)


def iter_(tree, path="", depth=1):
    children = tree.get("children")
    formatted_value = format_value(tree.get("value"))
    formatted_value1 = format_value(tree.get("value1"))
    formatted_value2 = format_value(tree.get("value2"))

    if tree["type"] == "root":
        lines = map(iter_, children)
        lines = filter(None, lines)
        return "\n".join(lines)
    if tree["type"] == "nested":
        nested_path = build_path(tree, path)
        lines = map(
            lambda child: iter_(child, nested_path, depth + 1), children
        )
        lines = filter(None, lines)
        return "\n".join(lines)
    if tree["type"] == "added":
        return "Property '{0}' was added with value: {1}".format(
            build_path(tree, path), formatted_value
        )
    if tree["type"] == "removed":
        return "Property '{}' was removed".format(build_path(tree, path))
    if tree["type"] == "modified":
        return "Property '{0}' was updated. From {1} to {2}".format(
            build_path(tree, path),
            formatted_value1,
            formatted_value2,
        )


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, dict):
        return "[complex value]"
    if value == 0:
        return "0"
    return "'{}'".format(value)  # for other data types


def build_path(source, path):
    if path:
        return ".".join([path, source["key"]])
    else:
        return source["key"]
