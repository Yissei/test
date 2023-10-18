import schedule as sch
from time import sleep
from plyer import notification

#アラーム設定・実行
def RunAlarm(setTime,message):
    job = sch.every().day.at(setTime).do(OutNotice, setTime=setTime, message=message)
    while True:
        if job.should_run:
            job.run()
            break
        sleep(1)

#通知表示　ログにも出力したいかも
def OutNotice(setTime, message):
    notification.notify(
        title = setTime,
        message = message,
        app_name = "スケジュール君",
        app_icon = "C:\\Windows\\WinSxS\\amd64_microsoft-windows-dxp-deviceexperience_31bf3856ad364e35_10.0.22621.1_none_a8baf777ed856ee0\\pictures.ico",
        timeout = 10
    )