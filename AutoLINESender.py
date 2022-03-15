import requests
from datetime import datetime
import time


def autoLINESender():
    file_path = input('Enter the token file path you want to use. >>')

    #f.closeを兼ねたopen()
    with open(file_path) as f:
        token_list = f.readlines()
        TOKEN = token_list[0]

    api_url = 'https://notify-api.line.me/api/notify'
    send_content = input('Enter the content you want to send. >>')

    # 送りたい内容は辞書型にしてAPIに渡す
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN} # Authorizationは固定キー  # Bearer後の半角スペースは必須
    send_content_dic = {'message': send_content} # messageは固定キー

    # 指定時刻が数字かどうか判定
    send_time = input('Enter time you want to send.  (ex.2022 April 1 12:00:00 => 20220401120000) >>')
    for i in range(3):
        try:
            send_time = int(send_time)
        except Exception:
            print('Error!: Invalid Value. Please again.')
            send_time = input('Enter time you want to send. (ex.2022 April 1 12:00:00 => 20220401120000) >>')
        else:
            break

    # 指定時刻を
    t = str(send_time)
    year = t[0:4]
    month = t[4:6]
    day = t[6:8]
    hour = t[8:10]
    minute = t[10:12]
    second = t[12:14]
    t = year + '/' + month + '/' + day + '-' + hour + ':' + minute + ':' + second
    print(f'Reserved: {t}')\

    while True:
        dt = datetime.now() # 現在時刻の取得
        now = dt.strftime('%Y/%m/%d-%H:%M:%S')
        print(now)
        if (t < now):
            print('Wrong time specification. Please try again.')
            break
        if (t == now):
            # 自分のLINEに通知を送る(200: Success, 400: Bad Request, 401: Invalid AccessToken)
            requests.post(api_url, headers=TOKEN_dic, data=send_content_dic)
            print('Sent the message successfully!')
            print(f'Content: {send_content}')
            break
        time.sleep(1) # １秒ずつカウント


# 実行
if __name__ == "__main__":
    autoLINESender()
