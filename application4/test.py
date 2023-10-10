#スケジュールjob用モジュール
#return でsch.cansel_jobを返さないと、定期実行されてしまう為、1回1回終了させる
import schedule as sch

def job(args):
    print("設定時刻 = " + args)
    return True