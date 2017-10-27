# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host = "smtp.badtom.cn"  # 设置服务器
mail_user = "admin@badtom.cn"  # 用户名
mail_pass = "Password123"  # 口令 
 
 
sender = 'admin@badtom.cn'
receivers = ['admin@badtom.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
# message = MIMEText('Python，你好', 'plain', 'utf-8')

mail_msg = """
<p>Python 邮件发送.</p>
<p><a href="http://www.badtom.cn">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')

message['From'] = Header("admin@badtom.cn", 'utf-8')
message['To'] = Header("admin@badtom.cn", 'utf-8')
 
subject = '给喵金币'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException, e:
    print str(e)
    print "Error: 无法发送邮件"
