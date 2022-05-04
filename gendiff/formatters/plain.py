def plain(source, path=[], depth=1, first_lvl_keys=None):
    if not first_lvl_keys:
        first_lvl_keys = list(source.keys())
    result = []

    for key, (type, *values) in sorted(source.items()):
        path.append(key)
        if type == "nested":
            result.append(plain(values[0], path, depth + 1, first_lvl_keys))
            if key in first_lvl_keys and depth == 1:
                path.clear()
            else:
                del path[-1::depth]

        elif type == "added":
            result.append(
                "Property '{}' was added with value: {}".format(
                    ".".join(path), format_value(values[0])
                )
            )
            del path[-1::depth]

        elif type == "removed":
            result.append("Property '{}' was removed".format(".".join(path)))
            del path[-1::depth]

        elif type == "modified":
            result.append(
                "Property '{}' was updated. From {} to {}".format(
                    ".".join(path),
                    format_value(values[0]),
                    format_value(values[1]),
                )
            )
            del path[-1::depth]
        else:
            del path[-1::depth]

    return "\n".join(result)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return "null"

    if isinstance(value, dict):
        return "[complex value]"

    return "'{}'".format(value)
