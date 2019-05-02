#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# py2需要加这一段转一下编码
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# 目标url
start_url = 'https://join.qq.com/center.php'
# 自定义headers
headers = {
			"Host": "join.qq.com",
			"Connection": "keep-alive",
			"Cache-Control": "max-age=0",
			"Upgrade-Insecure-Requests": "1",
			"Cookie": "" # 这里记得去copy
		}
my_sender = 'xxxxx@qq.com'  # 发件人邮箱账号
my_pass = 'xxxxxxxxxxxxxxxx'  # 发件人邮箱的smtp授权码
my_recevicer = 'xxxxx@qq.com'  # 收件人邮箱账号，可发送给自己


def mail(text):
	ret = True
try:
		msg = MIMEText(text, 'plain', 'utf-8')
		msg['From'] = formataddr(["From TonyRobot", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
		msg['To'] = formataddr(["tony", my_recevicer])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject'] = "腾讯，再爱我一次"  # 邮件的主题，也可以说是标题

		server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
		server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
		server.sendmail(my_sender, [my_recevicer, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()  # 关闭连接
	except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
		ret = False
	return ret


if __name__ == "__main__":
	while True:
		response = requests.get(url=start_url, headers=headers)
		if response.text.find("HR面试") == -1: # 这里因为在等HR面状态变为已完成，所以很暴力
			while mail(response.text) == False:
				time.sleep(10)
			break
		nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(nowTime+" nothing...")
		time.sleep(60)
