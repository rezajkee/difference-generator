def plain(source, path=[], depth=1):
    result = []

    if source["type"] == "root":
        for item in source["children"]:
            result.append(plain(item))

    elif source["type"] == "nested":
        path.append(source["key"])
        for item in source["children"]:
            result.append(plain(item, path, depth + 1))
        del path[-1::depth]

    elif source["type"] == "added":
        path.append(source["key"])
        result.append(
            "Property '{}' was added with value: {}".format(
                ".".join(path), format_value(source["value"])
            )
        )
        del path[-1::depth]

    elif source["type"] == "removed":
        path.append(source["key"])
        result.append("Property '{}' was removed".format(".".join(path)))
        del path[-1::depth]

    elif source["type"] == "modified":
        path.append(source["key"])
        result.append(
            "Property '{}' was updated. From {} to {}".format(
                ".".join(path),
                format_value(source["value1"]),
                format_value(source["value2"]),
            )
        )
        del path[-1::depth]

    result = filter(bool, result)
    return "\n".join(result)


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
