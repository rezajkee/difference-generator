import json
import yaml


def parse(data, format_name):
    if format_name in ["json", "JSON"]:
        return json.load(data)
    if format_name in ["yaml", "yml", "YML"]:
        return yaml.safe_load(data)
    raise ValueError(
        """"{}" file format not found.
        Format should be "json", "yaml" or "yml".""".format(
            format_name
        )
    )
