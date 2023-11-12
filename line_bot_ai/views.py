from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import message_creater
from line_bot_ai.line_message import LineMessage

#csrf無効
@csrf_exempt
def index(request):
    if request.method == 'POST':
        #デコード
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        #メッセージ受信
        message = data['message']
        reply_token = data['replyToken']
        #送信用テキスト作成後LINEmessageAPIへリクエスト
        line_message = LineMessage(message_creater.create_single_text_message(message['text']))
        #返信
        line_message.reply(reply_token)
        return HttpResponse("ok")
