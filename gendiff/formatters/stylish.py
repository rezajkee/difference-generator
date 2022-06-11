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
        return f"{{\n{result}\n}}"

    if tree["type"] == "nested":
        lines = map(lambda child: iter_(child, depth + 1), children)
        result = "\n".join(lines)
        return f"{indent}  {tree['key']}: {{\n{result}\n{indent}  }}"

    if tree["type"] == "modified":
        old_val = f"{indent}- {tree['key']}: {formatted_value1}"
        new_val = f"{indent}+ {tree['key']}: {formatted_value2}"
        return f"{old_val}\n{new_val}"

    if tree["type"] == "added":
        return f"{indent}+ {tree['key']}: {formatted_value}"

    if tree["type"] == "removed":
        return f"{indent}- {tree['key']}: {formatted_value}"

    if tree["type"] == "unmodified":
        return f"{indent}  {tree['key']}: {formatted_value}"


def build_indent(depth):
    return ' ' * (depth * 4 - 2)


def stringify(value, depth=1):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return "null"
    if isinstance(value, dict):
        parts = []
        for key in value:
            indent = build_indent(depth + 1)
            formatted_value = stringify(value[key], depth + 1)
            parts.append(f"{indent}  {key}: {formatted_value}")
        output = '\n'.join(parts)
        return f"{{\n{output}\n{build_indent(depth)}  }}"
    return value
