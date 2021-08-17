"""Seeds the database"""

import os
import json

#open up json file and parse through it, item by item
#figure out how to connect it to model.py

# with open('data/evictions.json') as f: #this syntax is from the lab
eviction_data = json.loads(open('data/evictions.json').read())

print(eviction_data)
# evictions_json = open('data/evictions.json').read()
# print(evictions_json)

