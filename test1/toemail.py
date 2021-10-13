import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManage(object):

    def __init__(self, filename):
        self.filename = filename

    def send_email(self):
        # 定义SMTP服务器
        smtpserver = 'smtp.163.com'

        # 发送邮件的用户名和客户端密码
        username = 'zmz1054920870@163.com'
        password = 'UPZMWDCEBQULAMUL'

        # 接收邮件的邮箱
        reveiver = '1054920870@qq.com'

        # 邮件的标题或者主题
        subject = '淘宝接口自动化测试报告'

        # 创建邮箱内容对象
        message = MIMEMultipart('related')

        # 邮件的附件，主要用于发送测试报告
        fujian = MIMEText(_text=open(self.filename, 'rb').read(), _subtype='html', _charset='utf8')

        # 添加邮箱内容
        message['from'] = username
        message['to'] = reveiver
        message['subject'] = subject
        message.attach(fujian)

        # 登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # connect(self, host='localhost', port=0, source_address=None):

        smtp.login(username, password)
        smtp.sendmail(username, reveiver,
                      message.as_string())  # (self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[]):

        # 发送完成以后我们就退出这个服务器
        smtp.quit()