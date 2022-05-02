def get_diff(file1, file2):
    diff = {}
    current_keys = file1.keys() | file2.keys()
    for key in current_keys:
        if key not in file2.keys():
            diff[key] = ("removed", file1[key])
        elif key not in file1.keys():
            diff[key] = ("added", file2[key])
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff[key] = ("nested", get_diff(file1[key], file2[key]))
        elif file1[key] == file2[key]:
            diff[key] = ("same", file1[key])
        elif file1[key] != file2[key]:
            diff[key] = ("modified", file1[key], file2[key])
    return diff
