#作者    ：YCKJ1130   

#创建时间：2020/6/23 16:44  

#文件    ：send_mail.py

#编译器  ：PyCharm

# import smtplib
# import time
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
#
# #邮件发送的用户名和密码    常识：第三方授权码
#
# _user='liuxuanyu_zyl@qq.com'
# _pwd='wrowicodhijhbcgd'
#
# now=time.strftime("%a,%d %b %Y %H:%M:%S %z")  #获取时间戳
#
# class SendMail:
#     def sendmail(self,email_to,filepath):
#         #mail_to 收件方
#         #file 你要发送的邮件地址
#         #如名字所示Multipart是分多个部分
#         msg=MIMEMultipart()
#         msg['Subject'] = now+"蛋挞的测试报告"
#         msg['From'] = _user
#         msg['To'] = email_to
#         msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
#         #-----这是文字部分-----
#         part=MIMEText('自动化测试报告，请查收')
#         msg.attach(part)
#         #-----这是附件部分-----只能发文件不能发文件夹
#         path=[]
#         for item in path:
#             part=MIMEApplication(open(item,'rb').read())
#             part.add_header('Content-Disposition','attachment',filename=filepath)
#             msg.attach(part)
#         s=smtplib.SMTP_SSL('smtp.qq.com',timeout=30)  #连接smtp服务器，端口默认25
#         s.login(_user,_pwd)  #登录服务器
#         s.sendmail(_user,email_to,msg.as_string())  #发送邮件
#         s.close()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
with open(r'E:\python_file\review\test_result\report.html','rb') as f:
    mail_body=f.read()
class SendMail:
    '''==========发送html==========='''
    def send_html(self):
        mail_host = "smtp.qq.com"  # QQ邮箱服务器
        from_addr = "liuxuanyu_zyl@qq.com"  # 发件人电子邮箱
        from_pwd = "wrowicodhijhbcgd"  # SMTP授权码
        to_addrs = 'liuxuanyu_zyl@qq.com'  # 收件人电子邮箱
        #创建邮件对象
        msg=MIMEMultipart()
        subject =Header('Python SMTP 邮件测试','utf-8').encode()
        msg["Subject"] = subject    #设置邮件主题
        text = mail_body
        msg['From'] = from_addr    #设置邮件发送者
        msg['To'] = to_addrs     #设置邮件接收者
        html = MIMEText(text, 'html', 'utf-8')   #添加html
        msg.attach(html)
        try:
            #登录邮箱
            #1、连接邮箱服务器
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 服务器地址，465 为SMTP端口号
            #2、登录邮箱
            smtpObj.login(from_addr, from_pwd)  #邮箱账号和密码
            smtpObj.sendmail(from_addr, to_addrs, msg.as_string())
            smtpObj.quit()  # 关闭连接
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error：无法发送邮件")


    '''=========发送附件=========='''

    def send_file(self):
        mail_host = "smtp.qq.com"  # QQ邮箱服务器
        from_addr = "liuxuanyu_zyl@qq.com"  # 发件人电子邮箱
        from_pwd = "wrowicodhijhbcgd"  # SMTP授权码
        to_addrs = 'liuxuanyu_zyl@qq.com'  # 收件人电子邮箱
        #创建邮件对象
        msg=MIMEMultipart()
        subject =Header('Python SMTP 邮件测试','utf-8').encode()
        msg["Subject"] = subject    #设置邮件主题
        text = mail_body
        msg['From'] = from_addr    #设置邮件发送者
        msg['To'] = to_addrs     #设置邮件接收者
        file1 = MIMEText(text, 'base64', 'utf-8')   #添加html
        file1['Content-Disposition']='attachment;filename="test_api.html"'
        msg.attach(file1)
        try:
            #登录邮箱
            #1、连接邮箱服务器
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 服务器地址，465 为SMTP端口号
            #2、登录邮箱
            smtpObj.login(from_addr, from_pwd)  #邮箱账号和密码
            smtpObj.sendmail(from_addr, to_addrs, msg.as_string())
            smtpObj.quit()  # 关闭连接
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error：无法发送邮件")
if __name__ == '__main__':
    SendMail().send_file()


