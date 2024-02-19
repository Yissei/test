#コマンドライン引数・PG終了用
import sys
#pause用
import os
#json読込用
import ComJson as cj

#処理終了判定用フラグ
endFlg = True
#コマンドライン引数を取得
args = sys.argv

if (len(args) == 1):
    #処理モード 0:通常 1:コマンドプロンプトのみ 2:PowerShellのみ
    procType = 0
else:
    #コマンドライン引数より、処理モード判定
    if (args[1] == "-c"):
        #-cの場合、コマンドプロンプトの内容のみ表示
        procType = 1
    elif (args[1] == "-p"):
        #-pの場合、コマンドプロンプトの内容のみ表示
        procType = 2
    else:
        #それ以外の場合は通常
        procType = 0

#jsonよりコマンド一覧を取得し、一覧表示用リストに格納
cmdList = []
if(procType == 0):
    cmdList.extend(cj.getAllKey(cj.SEC_CMD))
    cmdList.extend(cj.getAllKey(cj.SEC_POW))
elif(procType == 1):
    cmdList.extend(cj.getAllKey(cj.SEC_CMD))
elif(procType == 2):
    cmdList.extend(cj.getAllKey(cj.SEC_POW))

inputValue = ""
while endFlg:
    print("\n------------------------------------------------------")
    for cntI in range(len(cmdList)):
        print(str(cntI + 1) + ":" + str(cmdList[cntI]))
    print("\nコマンドを番号で選択\n\"end\"と入力で処理終了")
    inputValue = input()
    if (inputValue == "end"):
        endFlg = False
    else:
        #入力値チェック
        if not str.isdecimal(inputValue):
            #数値以外の場合
            print("画面に表示された番号を入力してください\n")
            os.system("PAUSE")
            continue
        if (int(inputValue) < 1) or (int(inputValue) > len(cmdList)):
            #インデックスを超える、もしくは1より小さい場合
            print("指定された番号は存在しません\n")
            os.system("PAUSE")
            continue
        #入力された番号のコマンドに関する情報をjsonより取得
        #strCmdName = cmdList[inputValue - 1]        
        cmdName = cmdList[int(inputValue) - 1] #コマンド名
        syntax = "" #構文
        summary = "" #概要
        
        #概要、構文を取得
        summary = cj.getValue(cj.SEC_CMD, str(cmdList[int(inputValue) - 1]), cj.KEY_SUMMARY)
        if summary is None:
            summary = cj.getValue(cj.SEC_POW, str(cmdList[int(inputValue) - 1]), cj.KEY_SUMMARY)
            if summary is None:
                summary = "ERROR"
        syntax = cj.getValue(cj.SEC_CMD, str(cmdList[int(inputValue) - 1]), cj.KEY_SYNTAX)
        if syntax is None:
            syntax = cj.getValue(cj.SEC_POW, str(cmdList[int(inputValue) - 1]), cj.KEY_SYNTAX)
            if syntax is None:
                syntax = "ERROR"

        syntaxArray = str(syntax).split(",")
        syntax = ""
        for cntJ in range(len(syntaxArray)):
            if cntJ == 0:
                syntax += "\n      構文 = " + syntaxArray[cntJ]
            else:
                syntax += "\n             " + syntaxArray[cntJ]
        print("\n" + "コマンド名 = " + str(cmdName) + "\n      概要 = " + str(summary) + str(syntax) + "\n")
        os.system("PAUSE")