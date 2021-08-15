import sys
import math

# コマンド引数要素をint型に変換
def conv_int(cmd_params):
    int_params = list(map(int,cmd_params))
    return int_params

def circle_area(int_params):
    radius = int_params[0]
    return math.pi * radius * radius

## 実行 ##

# コマンドライン引数の取得
# 引数先頭のファイル名はスライスで除外
cmd_params = sys.argv[1:]


#コマンド引数が10進法の数字なら
if "".join(cmd_params).isdecimal() == True:
    #要素をint型に変換し
    params = conv_int(cmd_params)

    print(circle_area(params))

elif cmd_params == []:
    print("入力値がありません")
else:
    print("数字を入力してください")
