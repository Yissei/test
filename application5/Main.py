#コマンドライン引数・PG終了用
import sys
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
            print("数値を入力してください")
            continue
        #入力された番号のコマンドに関する情報をjsonより取得
        #strCmdName = cmdList[inputValue - 1]
        print(cmdList[int(inputValue) - 1][""])