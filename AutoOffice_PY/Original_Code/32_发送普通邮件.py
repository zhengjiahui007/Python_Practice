# smtplib
# email
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 登录邮箱
smtp_obj = smtplib.SMTP("smtp.qq.com")
smtp_obj.login('398707160@qq.com','ppzuouwejpuebgfg')
# 编辑内容
mail_text = 'This is Email~ 你要的邮件来啦'
msg_body = MIMEText(mail_text,'plain','utf-8')
msg_body['From'] = Header('测试部门','utf-8')
msg_body['Subject'] = Header('测试邮件','utf-8')
# 发邮件
smtp_obj.sendmail('398707160@qq.com',['hotelmail@126.com'],msg_body.as_string())