#!/usr/bin/env python

def bool_to_json_format(string):
  if string.find(": False"):
    string = string.replace(": False", ": false")
  if string.find(": True"):
    string = string.replace(": True", ": true")
  if string.find(": None"):
    string = string.replace(": None", ": null")
  return string


import json


def generate_diff(file1path, file2path):
  file1 = json.load(open(file1path))
  file2 = json.load(open(file2path))

  deltas_in_first = {i: file1[i] for i in file1 if i in file2 and file1[i] != file2[i]}

  deltas_in_second = {i: file2[i] for i in deltas_in_first}

  no_diff = dict(file1.items() & file2.items())

  removed = file1.keys() - file2.keys()
  removed = {i: file1[i] for i in removed}

  added = file2.keys() - file1.keys()
  added = {i: file2[i] for i in added}

  keys_in_file1 = {i for i in file1}
  keys_in_file2 = {i for i in file2}
  all_keys = keys_in_file1 | keys_in_file2

  list_of_keys = list(all_keys)
  list_of_keys.sort()
  result = '{\n'
  for i in list_of_keys:
    if i in no_diff:
      result += '   {}: {}\n'.format(i, no_diff[i])
    if i in deltas_in_first:
      result += ' - {}: {}\n'.format(i, deltas_in_first[i])
    if i in deltas_in_second:
      result += ' + {}: {}\n'.format(i, deltas_in_second[i])
    if i in removed:
      result += ' - {}: {}\n'.format(i, removed[i])
    if i in added:
      result += ' + {}: {}\n'.format(i, added[i])
  result += '}'
  return(bool_to_json_format(result))
