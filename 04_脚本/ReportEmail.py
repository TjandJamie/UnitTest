import unittest
from ReadData.HTMLTestRunner import HTMLTestRunner
import time
import smtplib                           #发送邮件模块
from email.mime.text import MIMEText    #定义邮件内容
from email.header import Header         #定义邮件标题
import os

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver='smtp.126.com'
    # 发送邮箱用户名
    user = 'liuguoyun1@126.com'
    # 邮箱授权码
    password = 'test002'

    # 发送和接收邮箱
    sender = ' liuguoyun1@126.com'
    receives = [' liuguoyun1@126.com', '150691555@qq.com']

    # 发送邮件主题和内容
    subject = '三角形单元测试报告'

    # HTML邮件正文
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("Start send Email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send Email end!")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print(("new report is :" + lists[-1]))

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    test_dir='./'
    report_dir='../Report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + '/' + now + 'report.html'

    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="三角形测试测试报告", description="三角形覆盖率100%")
        runner.run(discover)

    #h获取最新测试报告
    latest_report=latest_report(report_dir)
    #发送邮件报告
    send_mail(latest_report)

'''
    # 行内行数
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    
    
    def key(fn):
        return os.path.getatime(report_dir + '\\' + fn)

'''