#!/usr/bin/env python

import json
import yaml


def parse(path):
    if path.endswith('.json'):
        return json.load(open(path))
    if path.endswith('.yaml') or path.endswith('.yml'):
        return yaml.safe_load(open(path))
