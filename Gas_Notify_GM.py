import bs4
import time
import requests
import datetime
import setting
import schedule

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}

Target_URL_S = 'https://gogo.gs/shop/0299000043'
resp1 = requests.get(Target_URL_S, headers=headers)
resp1.raise_for_status()
now1 = datetime.datetime.now().strftime('%Y年%m月%d日')
soup1 = bs4.BeautifulSoup(resp1.text, "html.parser")
shop1 = soup1.find_all(class_="title")[0].text.replace(' ','')
entries1 = soup1.find_all(class_="price-card")
oil1 = entries1[0].find(class_="mode-label").text
price1 = entries1[0].find(class_="price").text
confirm1 = entries1[0].find(class_="date").text
message_s = f'\n{shop1}{oil1}の価格は{price1}円です\n({confirm1})'
print( f'\n{shop1}{oil1}の価格は{price1}円です\n({confirm1})')

Target_URL_Y = 'https://gogo.gs/shop/0299000087'
resp2 = requests.get(Target_URL_Y, headers=headers)
resp2.raise_for_status()
now2 = datetime.datetime.now().strftime('%Y年%m月%d日')
soup2 = bs4.BeautifulSoup(resp2.text, "html.parser")
shop2 = soup2.find_all(class_="title")[0].text.replace(' ','')
entries2 = soup2.find_all(class_="price-card")
oil2 = entries1[0].find(class_="mode-label").text
price2 = entries1[0].find(class_="price").text
confirm2 = entries1[0].find(class_="date").text
message_y = f'今日の{shop2}{oil2}の価格は{price2}円です\n({confirm2})'
print( f'今日の{shop2}{oil2}の価格は{price2}円です\n({confirm2})\nhttps://gogo.gs/shop/0299000087')

message = message_y + message_s

TOKEN = setting.AP_GM

def main():
    send_line_notify(
      message
    )

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = TOKEN
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'\n{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)
    time.sleep(1)

if __name__ == "__main__":
    main()

schedule.every().day.at("08:00").do(main, send_line_notify)

while True:
    schedule.run_pending()