import json

#適当な辞書型(jsonは辞書型に対応)
sampleDict = {
                "A":"red",
                "B":"blue",
                "C":"yellow"
                }

#with文でくくると、open→処理後、必ず閉じてくれるので便利
#読込ではなく書き込みなので、"w"。また、ファイルが存在しない場合も勝手に作ってくれる
with open("./sample.json", "w") as json_open:
    #indentを指定すると、json書き込みファイルが改行される
    json.dump(sampleDict, json_open, indent=4)