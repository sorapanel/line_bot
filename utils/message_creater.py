#送信メッセージ作成
def create_single_text_message(message):
    if message is not None:
        #文字数カウント
        message = str(len(message)) + '文字です(空白を含む)\n' + str(len(message.replace('　', '').replace('\t', '').replace('\n', ''))) + '文字です(空白を含まない)'

    #送信用形式
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message
