# -*- coding: utf-8 -*-

# Python script to Read file from JSON and convert to YAML
# Author - yucheng.hu@insight.com

import json

import ruamel.yaml as yaml

json_filename = 'resources/honeymoose_test.json'
yaml_filename = 'resources/honeymoose_test.yaml'

# Read and process JSON
with open(json_filename) as json_file:
    data = json.load(json_file)
    print(type(data))

    for data_dict in data:
        label_id = data_dict['label_id']
        print(str(label_id))

print(json_file.closed)

# Using with write to YAML
with open(yaml_filename, 'w') as yaml_file:
    yaml.dump(data, yaml_file, allow_unicode=True)
