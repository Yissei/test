import datetime
import CommonJson as cj
import ScheduleProp as sp
import OutNotice as on

#システム日付を取得
today = format(datetime.date.today(), "%Y/%m/%d")
#jsonから本日のスケジュールを読込、プロパティに設定
schTimeList = cj.getAllKey(today)
schMessageList = []
schProps = []
cntI = 0
for i in range(len(schTimeList)):
    schMessageList.append(cj.getValue(today, schTimeList[cntI]))
    schProps.append(sp.ScheduleData(schTimeList[cntI],schMessageList[cntI]))
    on.RunAlarm(str(schProps[cntI].GetSchTime()), str(schProps[cntI].GetSchMessage()))
    cntI += 1