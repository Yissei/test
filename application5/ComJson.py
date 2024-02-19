import json
import os

#定数
JSON_PATH = ".\\cmd.json"
SEC_CMD = "CmdPrompt"
SEC_POW = "PowerShell"
KEY_SUMMARY = "summary"
KEY_SYNTAX = "syntax"

#全てのキーを取得
def getAllKey(section):
    json_open = open(JSON_PATH, encoding="utf-8", mode="r")
    json_load = json.load(json_open)
    return list(json_load[section].keys())

#セクションとキー１、キー２を指定し、値を取得
def getValue(section, key1, key2):
    try:
        json_open = open(JSON_PATH, encoding="utf-8", mode="r")
        json_load = json.load(json_open)
        return json_load[section][key1][key2]
    except:
        return None