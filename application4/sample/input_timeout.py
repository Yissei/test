#参考サイト→https://www.delftstack.com/ja/howto/python/python-input-with-timeout/
#python.exe -m pip install --upgrade pip
#pip install inputimeout
from inputimeout import inputimeout, TimeoutOccurred
from time import sleep
import sys

run = False
firstRunMode = True
value = ""
while True:
    try:
        #ここでリマインダーが動作可能か確認する（"w"が入力される = inputモードに戻る　という風にしたい）
        if(value=="w"):
            print("wと入力された")
        elif(value=="end"):
            sys.exit(0)
        else:
            print("w以外が入力、もしくはtimeout")
        #初回のみコンソールに表示したい文があればここで表示
        if (firstRunMode):
            print("\"w\"と入力(終了する場合は\"end\")")
            firstRunMode = False
        #timeout後、except TimeoutOccurredへ移行
        #入力されなかった場合→TimeoutOccurredのcontinueで、またwhile文の頭に戻って来るので、恐らくsleep(1)が不要となる
        value = inputimeout(timeout=5)

    #timeout後にここに来る
    #この中でcontinueをする事で、リマインダー動作確認処理のwhile文先頭に戻す事ができる
    #while文の中でtry catchを作る必要がある
    except TimeoutOccurred:
        continue