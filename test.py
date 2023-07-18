import os
import shutil as sh
import datetime as dt

PATH_A = "C:\\private\\a\\"
PATH_B = "C:\\private\\b\\"
FILE_NAME = "saved"

today = format(dt.date.today(),"%Y%m%d")

#ディレクトリのコピーはcopytree　第1引数に元ディレクトリ、第2引数に先ディレクトリ
sh.copytree(PATH_A + FILE_NAME, PATH_B + FILE_NAME + "_" + today)

#処理結果 :　C:\private\b\saved_YYYYmmdd　が生成される