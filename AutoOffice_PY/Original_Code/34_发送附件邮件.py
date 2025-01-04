# smtplib
# email
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

# 登录邮箱
smtp_obj = smtplib.SMTP("smtp.qq.com")
smtp_obj.login('398707160@qq.com','ppzuouwejpuebgfg')
# 编辑内容
mail_text = '''
<h1 style="color:red">这个是一个HTML邮件</h1>
<p>这是邮件的主题内容</p>
<p><a href="http://www.itbaizhan.cn">这个是链接</a></p>
'''
# 编写文本内容
msg_body = MIMEText(mail_text,'html','utf-8')
# 增加附件
file = MIMEApplication(open('./create_data/21_word2pdf.pdf','rb').read())
file.add_header('Content-Disposition','attachment',filename='wp.pdf')
# 封装邮件主体
multi_part =MIMEMultipart()
multi_part.attach(msg_body)
multi_part['From'] = Header('测试部门','utf-8')
multi_part['Subject'] = Header('测试附件邮件','utf-8')
multi_part.attach(file)

# 发邮件
smtp_obj.sendmail('398707160@qq.com',['hotelmail@126.com'],multi_part.as_string())