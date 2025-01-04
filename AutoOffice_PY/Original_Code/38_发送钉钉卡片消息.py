def send_card():
    from dingtalkchatbot.chatbot import DingtalkChatbot,CardItem
    url = 'https://oapi.dingtalk.com/robot/send?access_token=8759abb5e065a51da329a7a057213c7765b19631663199910c20b8dbf10ec5d9'
    bot = DingtalkChatbot(url,secret='SEC73ae2091595da6118bcf20351cbb89959325e54babf079ff4b4016b837aedaa5')


    card1 = CardItem(title="氧气美女", url="http://www.itbaizhan.cn", pic_url='http://pic.netbian.com/uploads/allimg/190824/212516-1566653116f355.jpg')
    card2 = CardItem(title="氧眼美女", url="http://www.itbaizhan.cn", pic_url='http://pic.netbian.com/uploads/allimg/201112/000443-16051106836aa6.jpg')
    card3 = CardItem(title="氧神美女", url="http://www.itbaizhan.cn", pic_url='http://pic.netbian.com/uploads/allimg/190824/205524-15666513248366.jpg')
    cards = [card1, card2, card3]

    bot.send_feed_card(cards)

def send_card2():
    from dingtalkchatbot.chatbot import DingtalkChatbot,CardItem,ActionCard
    url = 'https://oapi.dingtalk.com/robot/send?access_token=8759abb5e065a51da329a7a057213c7765b19631663199910c20b8dbf10ec5d9'
    bot = DingtalkChatbot(url,secret='SEC73ae2091595da6118bcf20351cbb89959325e54babf079ff4b4016b837aedaa5')
    # Link消息
    # ActionCard整体跳转消息类型
    btns1 = [CardItem(title="查看详情", url="https://www.itbaizhan.cn/")]
    actioncard1 = ActionCard(title='万万没想到，竟然...',
                                text='![选择](http://pic.netbian.com/uploads/allimg/201112/000443-16051106836aa6.jpg) \n### 故事是这样子的...',
                                btns=btns1,
                                btn_orientation=1,
                                hide_avatar=1)
    bot.send_action_card(actioncard1)

def send_card3():
    from dingtalkchatbot.chatbot import DingtalkChatbot,CardItem,ActionCard
    url = 'https://oapi.dingtalk.com/robot/send?access_token=8759abb5e065a51da329a7a057213c7765b19631663199910c20b8dbf10ec5d9'
    bot = DingtalkChatbot(url,secret='SEC73ae2091595da6118bcf20351cbb89959325e54babf079ff4b4016b837aedaa5')
    # Link消息
    # ActionCard独立跳转消息类型（双选项）
    btns2 = [CardItem(title="支持", url="https://www.itbaizhan.cn/"), CardItem(title="反对", url="https://www.itbaizhan.cn/")]
    actioncard2=ActionCard(title='万万没想到，竟然...',text='![选择](http://pic.netbian.com/uploads/allimg/190824/205524-15666513248366.jpg) \n### 故事是这样子的...',
                                btns=btns2,
                                btn_orientation=1,
                                hide_avatar=1)
    bot.send_action_card(actioncard2)

def send_card4():
    from dingtalkchatbot.chatbot import DingtalkChatbot,CardItem,ActionCard
    url = 'https://oapi.dingtalk.com/robot/send?access_token=8759abb5e065a51da329a7a057213c7765b19631663199910c20b8dbf10ec5d9'
    bot = DingtalkChatbot(url,secret='SEC73ae2091595da6118bcf20351cbb89959325e54babf079ff4b4016b837aedaa5')
    # Link消息
    # ActionCard独立跳转消息类型（双选项）
    btns2 = [CardItem(title="支持", url="https://www.itbaizhan.cn/"),CardItem(title="中立", url="https://www.itbaizhan.cn/"),  CardItem(title="反对", url="https://www.itbaizhan.cn/")]
    actioncard2=ActionCard(title='万万没想到，竟然...',text='![选择](http://pic.netbian.com/uploads/allimg/190824/212516-1566653116f355.jpg) \n### 故事是这样子的...',
                                btns=btns2,
                                btn_orientation=1,
                                hide_avatar=1)
    bot.send_action_card(actioncard2)
if __name__ == "__main__":
    # send_card()
    # send_card2()
    # send_card3()
    send_card4()
    