#Plyerインストール
#pip install plyer

#notificationのnotify関数を使用
#引数は主に5つ。内容は以下
#notification.notify(
#    title="通知バナーのタイトル(str)",
#    message="メッセージの内容(str)",
#    app_name="通知を発行するアプリケーションの名前(str)",
#    app_icon="メッセージと共に通知バナーに表示するアイコン。フルパスで指定・拡張子は.ico(str)",
#    timeout="通知バナーを表示する時間(int)"
#)
#上記以外に、ticker、toast等の引数が存在する

#※実行しても通知が来ない場合、通知の設定がオフになっている可能性がある

#サンプル
from plyer import notification

#バナーの設定
notification.notify(
    title="test",
    message="message test",
    app_name="banner_out.py",
    app_icon="C:\\Windows\\WinSxS\\amd64_microsoft-windows-dxp-deviceexperience_31bf3856ad364e35_10.0.22621.1_none_a8baf777ed856ee0\\pictures.ico",
    timeout=10
)