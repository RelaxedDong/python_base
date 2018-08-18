#encoding:utf-8
# 发邮件的库
import smtplib
from email.mime.multipart import MIMEMultipart
#邮件文本
from email.mime.text import MIMEText

#SMTP服务器
SMTPServer = 'smtp.yeah.net'

Sender = 'pepper_hot@yeah.net'

#授权密码
Password = 'donghao19980122'

#设置接收者
reciver = ['1417766861@qq.com']

# 设置发送内容
message = MIMEMultipart()
message.attach(MIMEText('send with file...', 'plain', 'utf-8'))

#转换成邮件文本
message['From'] = Sender
message['Subject'] = '过来了'

att1 = MIMEText(open('timg.jpg', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="timg.jpg"'
message.attach(att1)


try:
    # 创建SMTP服务器
    smtpObj = smtplib.SMTP()
    #连接服务器
    smtpObj.connect(SMTPServer, 25)
    # 登录邮箱
    smtpObj.login(Sender, Password)
    smtpObj.sendmail(Sender, reciver,message.as_string())
    print('发送成功')
    smtpObj.quit()
except smtplib.SMTPException:
    print('发送失败')
