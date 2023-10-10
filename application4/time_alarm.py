#pipコマンドの最新化
#python.exe -m pip install --upgrade pip
#scheduleモジュールインストール
#pip install schedule

#PG終了用
import sys
#スケジュールモジュール
import schedule as sch
#sleep用
from time import sleep

#テスト用自作モジュール
import test

while True:
    #時刻入力
    print("時間を入力HH:MM(24時間表記)\n例 : 16:40")
    value = input()
    if(value == "exit"):
        sys.exit(0)
    else:
        #スケジュール登録 doの第1引数は関数名、第2引数に呼び出し元の引数変数名を参照し、各引数に値を設定する
        #ここで設定した時刻に関するスケジュールを変数に格納。他の時刻についても、同様に変数に入れる必要があるので、リストを使用するのが有効と思われる
        job = sch.every().day.at(value).do(test.job, args=value)

    #イベント実行
    while True:
        #変数jobに格納されたスケジュールが実行可能か確認し、実行できるならそのまま実行
        if job.should_run:
            #実行可能なスケジュールを実行。　→「job.run()」でも可能、こっちの方が各スケジュールに対応したスケジュールを実行できるかも？
            sch.run_pending()
            break
        print("イベント待機中")
        sleep(1)        