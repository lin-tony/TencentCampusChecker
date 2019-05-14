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
			"Cookie": "" 		# 这里记得去copy
		}
my_sender = 'xxxxx@qq.com'  	# 发件人邮箱账号
my_pass = 'xxxxxxxxxxxxxx'  	# 发件人邮箱的smtp授权码
my_recevicer = 'xxxxx@qq.com'   # 收件人邮箱账号，可发送给自己


def mail(text):
	ret = True
	try:
		msg = MIMEText(text, 'plain', 'utf-8')
		msg['From'] = formataddr(["From TonyRobot", my_sender])  # 发件人邮箱昵称、发件人邮箱账号
		msg['To'] = formataddr(["tony", my_recevicer])  # 收件人邮箱昵称、收件人邮箱账号
		msg['Subject'] = "腾讯，再爱我一次"  # 邮件标题

		server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器+端口
		server.login(my_sender, my_pass)  # 发件人邮箱账号、邮箱密码
		server.sendmail(my_sender, [my_recevicer, ], msg.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()  # 关闭连接
	except Exception:
		ret = False
	return ret


if __name__ == "__main__":
	while True:
		response = requests.get(url=start_url, headers=headers)
		if response.text.find("HR面试") == -1 or response.text.find("textgreen") == -1: # 等状态变为已完成或者变灰，自行更改
			while mail(response.text) == False: # 暴力重发
				time.sleep(10)
			break
		nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(nowTime+" nothing...")
		time.sleep(60)
