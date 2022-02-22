# -------------------------------------
# import package to read json
# import package to walk file system
# -------------------------------------
# python3 read_json_multiple.py

import json
import glob

# -----------------------------------
#  list all files
# -----------------------------------
pattern = './data/*/*.json'
data = []

for file in glob.glob(pattern):
    data.append(file)

print(data)
# -----------------------------------
#  loop through files, parse json
# -----------------------------------

def readJson(file):
    with open(file) as p:
        return json.load(p)

for file in data:
    file = readJson(file)
    print(file)