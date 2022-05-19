INDENT = " "
attach = {
    "added": "+",
    "removed": "-",
    "same": INDENT,
}


def stylish(source, depth=1, indent_count=2):
    result = []
    current_indent = INDENT * indent_count
    deep_indent = current_indent * depth

    def add_indent(attach_type, node):
        result.append(
            "{}{}{}{}: {}".format(
                deep_indent, attach[attach_type], INDENT, source["key"], node
            )
        )

    if source["type"] == "root":
        result.append("{")
        for item in source["children"]:
            result.append(stylish(item))
        result.append("}")

    elif source["type"] == "nested":
        add_indent("same", "{")
        for item in source["children"]:
            result.append(stylish(item, depth + 2))
        result.append("{}}}".format(current_indent + deep_indent))

    elif source["type"] == "modified":
        add_indent("removed", stringify(source["value1"], depth + 1))
        add_indent("added", stringify(source["value2"], depth + 1))

    else:
        add_indent(source["type"], stringify(source["value"], depth + 1))

    return "\n".join(result)


def stringify(value, depth=1, indent_count=2):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return "null"
    if isinstance(value, dict):
        result = ['{',
                  '{0}{1}'.format(INDENT * indent_count * depth, '}')]

        for key, val in value.items():
            indent_in_depth = INDENT * indent_count * (depth + 2)
            key_with_indent = indent_in_depth + str(key)
            result.insert(-1, '{0}: {1}'.format(
                key_with_indent, stringify(val, depth + 2)
            ))
        return '\n'.join(result)
    return value
