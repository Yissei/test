class ScheduleData:
    #コンストラクタ
    def __init__(self, schTime, schMessage):
        self.schTime = schTime
        self.schMessage = schMessage
    #アラーム設定時刻を返却
    def GetSchTime(self):
        return self.schTime
    #アラームメッセージ内容を返却
    def GetSchMessage(self):
        return self.schMessage