# pip install zmail 

def base_use():
    import zmail
    server = zmail.server('398707160@qq.com','ppzuouwejpuebgfg')

    info = {
        'subject':'这个是主题',
        'from':'这个是发送者<aaa>',
        'content_text':'这个Email的内容！！！！'
    }
    server.send_mail('hotelmail@126.com',info)

def base_file():
    import zmail
    server = zmail.server('398707160@qq.com','ppzuouwejpuebgfg')
    
    info = {
        'subject':'这个是主题',
        'from':'这个是发送者<aaa>',
        'content_text':'这个Email的内容！！！！',
        'attachments':['./create_data/21_word2pdf.pdf']
    }
    server.send_mail('hotelmail@126.com',info)

def base_html():
    import zmail
    server = zmail.server('398707160@qq.com','ppzuouwejpuebgfg')
    
    info = {
        'subject':'这个是主题',
        'from':'这个是发送者<aaa>',
        'content_html':'<h1>这个Email的内容！！！！</h1>',
        'attachments':['./create_data/21_word2pdf.pdf']
    }
    server.send_mail('hotelmail@126.com',info)

def get_mail():
    import zmail
    server = zmail.server('398707160@qq.com','vjgjkivjwjokcajc')

    last_mail = server.get_latest()
    print(last_mail.get('subject'))
    print(last_mail.get('from'))
    print(last_mail.get('to'))
    print(last_mail.get('content_text'))
    print(last_mail.get('content_html'))
    print(last_mail.get('date'))
    print(last_mail)    # 'content_text', 'content_html', 'attachments', 'headers', 'raw_headers', 'charsets', 'subject', 'date', 'from', 'to', 'id', 'raw'
if __name__ == "__main__":
    # base_use()
    # base_file()
    # base_html()
    get_mail()