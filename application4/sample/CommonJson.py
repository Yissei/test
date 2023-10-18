import json

path = "./Schedule.json"

def getAllKey(section):
    print(path)
    json_open = open(path, encoding="utf-8", mode="r")
    json_load = json.load(json_open)
    return list(json_load[section].keys())

def getValue(section, key):
    json_open = open(path, encoding="utf-8", mode="r")
    json_load = json.load(json_open)
    ret = json_load[section][key]
    return ret