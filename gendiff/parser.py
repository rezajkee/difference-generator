#!/usr/bin/env python

import json
import yaml


def parse(path):
    if path.endswith(('.json', '.JSON')):
        return json.load(open(path))
    if path.endswith(('.yaml', '.yml', '.YML')):
        return yaml.safe_load(open(path))
