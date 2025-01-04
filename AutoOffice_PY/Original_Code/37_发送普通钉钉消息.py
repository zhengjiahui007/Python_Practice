# pip install dingtalkchatbot
def send_text():
    from dingtalkchatbot.chatbot import DingtalkChatbot
    url = 'https://oapi.dingtalk.com/robot/send?access_token=8759abb5e065a51da329a7a057213c7765b19631663199910c20b8dbf10ec5d9'
    bot = DingtalkChatbot(url,secret='SEC73ae2091595da6118bcf20351cbb89959325e54babf079ff4b4016b837aedaa5')
    # bot.send_text('测试下消息!')
    # bot.send_text('你该交作业了！！',at_mobiles=['1770000000'])
    bot.send_text('同学们，该交作业了！！',is_at_all=True)

def send_img():
    from dingtalkchatbot.chatbot import DingtalkChatbot
    url = 'https://oapi.dingtalk.com/robot/send?access_token=8759abb5e065a51da329a7a057213c7765b19631663199910c20b8dbf10ec5d9'
    bot = DingtalkChatbot(url,secret='SEC73ae2091595da6118bcf20351cbb89959325e54babf079ff4b4016b837aedaa5')
    bot.send_image(pic_url='https://www.itbaizhan.cn/public/new/index/images/couimg1.jpg')

def send_link():
    from dingtalkchatbot.chatbot import DingtalkChatbot
    url = 'https://oapi.dingtalk.com/robot/send?access_token=8759abb5e065a51da329a7a057213c7765b19631663199910c20b8dbf10ec5d9'
    bot = DingtalkChatbot(url,secret='SEC73ae2091595da6118bcf20351cbb89959325e54babf079ff4b4016b837aedaa5')
    bot.send_link(title='Python自动化课程',text='欢迎收看Python课程',message_url='http://www.itbaizhan.cn',pic_url='https://www.itbaizhan.cn/public/new/index/images/couimg1.jpg')

def send_md():
    from dingtalkchatbot.chatbot import DingtalkChatbot
    url = 'https://oapi.dingtalk.com/robot/send?access_token=8759abb5e065a51da329a7a057213c7765b19631663199910c20b8dbf10ec5d9'
    bot = DingtalkChatbot(url,secret='SEC73ae2091595da6118bcf20351cbb89959325e54babf079ff4b4016b837aedaa5')
    bot.send_markdown(title='Python自动化课程',text='### 欢迎收看Python课程\n'
    '此次课程我们安排的是....'
    '![Python](https://www.itbaizhan.cn/public/new/index/images/couimg1.jpg)'
    )
if __name__ == "__main__":
    # send_text()
    # send_img()
    # send_link()
    send_md()