def collect(file1, file2):
    diff = []
    current_keys = sorted(file1.keys() | file2.keys())
    for key in current_keys:
        if key not in file2.keys():
            diff.append(
                {
                    "key": key,
                    "type": "removed",
                    "value": file1[key],
                }
            )
        elif key not in file1.keys():
            diff.append(
                {
                    "key": key,
                    "type": "added",
                    "value": file2[key],
                }
            )
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff.append(
                {
                    "key": key,
                    "type": "nested",
                    "children": collect(file1[key], file2[key]),
                }
            )
        elif file1[key] == file2[key]:
            diff.append(
                {
                    "key": key,
                    "type": "same",
                    "value": file1[key],
                }
            )
        elif file1[key] != file2[key]:
            diff.append(
                {
                    "key": key,
                    "type": "modified",
                    "value1": file1[key],
                    "value2": file2[key],
                }
            )
    return diff


def get_diff(file1, file2):
    return {"type": "root", "children": collect(file1, file2)}
