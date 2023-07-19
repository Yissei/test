#try-catch 処理例
class TestException(Exception):
    pass

try:
    a = 11
    if not a > 10:
        raise TestException("例外テスト")

except TestException as e:
    print(e)
else:
    print("a = " + str(a) + "\n適切な数値")
finally:
    print("処理終了")