import re
print("入力")
while True:
    value = input()
    ptn = "[0-9]{2}:[0-9]{2}"
    if (re.match(ptn, value)):
        print("一致")
    else:
        print("不一致")