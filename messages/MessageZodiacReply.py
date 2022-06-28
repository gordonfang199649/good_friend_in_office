import secrets

def reply_question() -> str:
    messages = ['請問您是什麼星座？', '可以告訴我你的星座嗎？', '告訴我你的星座，我幫你請教國師的指示🏃‍', 'あの..方便透露你的星座嗎...', '星座給我，我幫你問唐老師', '來~ 什麼星座？講給我聽聽']
    return secrets.choice(messages)

def reply_yes_or_no_question() -> str:
    messages = ['請問您是想詢問星座運勢嗎？', '這個功能只能查詢當天今日星座運勢，你想知道的話可以點「是」喔', '跟你確認一下，你是要問星座嗎？']
    return secrets.choice(messages)

def reply_zodiac_not_exists() -> str:
    messages = ['您輸入的星座不存在耶，要不要再重新輸入一次?', '這個星座我沒有聽過耶？是你發明的嗎？', '給你選項居然不按，太讓我失望了🥲，再給你一次機會', '告訴我你是不是輸入錯了，還是按鍵不會按啊！😡',
                '你確定你講的這個星座在黃道十二宮裡面嗎？']
    return secrets.choice(messages)
