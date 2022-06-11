def render_plain(tree):
    return iter_(tree)


def iter_(tree, path="", depth=1):
    children = tree.get("children")
    formatted_value = format_value(tree.get("value"))
    formatted_value1 = format_value(tree.get("value1"))
    formatted_value2 = format_value(tree.get("value2"))
    property_path = f"{path}{tree.get('key')}"

    if tree["type"] == "root":
        lines = map(iter_, children)
        lines = filter(None, lines)
        return "\n".join(lines)
    if tree["type"] == "nested":
        lines = map(
            lambda child: iter_(child, f"{property_path}.", depth + 1), children
        )
        lines = filter(None, lines)
        return "\n".join(lines)
    if tree["type"] == "added":
        return (f"Property '{property_path}' was added "
                f"with value: {formatted_value}")
    if tree["type"] == "removed":
        return f"Property '{property_path}' was removed"
    if tree["type"] == "modified":
        return (f"Property '{property_path}' was updated. "
                f"From {formatted_value1} to {formatted_value2}")


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, dict):
        return "[complex value]"
    if value == 0:
        return "0"
    return f"'{value}'"  # for other data types
