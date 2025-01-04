# smtplib
# email
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 登录邮箱
smtp_obj = smtplib.SMTP("smtp.qq.com")
smtp_obj.login('398707160@qq.com','ppzuouwejpuebgfg')
# 编辑内容
mail_text = '''
<h1 style="color:red">这个是一个HTML邮件</h1>
<p>这是邮件的主题内容</p>
<p><a href="http://www.itbaizhan.cn">这个是链接</a></p>
'''
msg_body = MIMEText(mail_text,'html','utf-8')
msg_body['From'] = Header('测试部门','utf-8')
msg_body['Subject'] = Header('测试邮件','utf-8')
# 发邮件
smtp_obj.sendmail('398707160@qq.com',['hotelmail@126.com'],msg_body.as_string())