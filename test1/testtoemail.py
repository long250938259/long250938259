import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_email_by_qq(to, file_name):
    mailserver = "smtp.163.com"
    sender = "long250938259@163.com"
    reciver = "250938259@qq.com"
    passwd= "DSKYGJIOVIYIKBGC"

    text_info = file_name
    text_sub = MIMEText(text_info, _subtype="plain", _charset="utf-8")

    message = MIMEMultipart("alternative")
    subject = 'python sendemail test successful'
    message['From'] = sender
    message['To'] = to
    message['subject'] = subject
    message.attach(text_sub)

    # txt_file = open(file_name, 'rb').read()
    # txt = MIMEText(txt_file, 'base64', 'utf-8')
    # txt["Content-Type"] = 'application/octet-stream'
    # # 以下代码可以重命名附件为hello_world.txt
    # txt.add_header('Content-Disposition', 'attachment', filename=file_name.split("\\")[-1])
    # message.attach(txt)



    try:
        server = smtplib.SMTP()
        server.connect(mailserver, 25)

        # server.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        # server.starttls()
        server.login(sender, passwd)
        server.sendmail(sender, reciver, message.as_string())
        server.quit()
        print('sendemail successful!')
    except Exception as e:
        print('sendemail failed next is the reason')
        print(e)


if __name__ == '__main__':
    # 可以是一个列表，支持多个邮件地址同时发送，测试改成自己的邮箱地址
    to = '250938259@qq.com'
    file = "D:\ll\ceshi1.txt"
    send_email_by_qq(to, file)