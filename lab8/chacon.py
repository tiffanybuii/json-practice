#!/usr/bin/env python3

import json

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)
    with open('chacon.csv', 'w') as file:
        for line in data[0:5]:
            file.write(line['name']+","+line['html_url']+","+line['updated_at']+","+line['visibility']+"\n")