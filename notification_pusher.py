
import config as cf
import requests


def notification_pusher(summary:str, message: str):
    if cf.NOTIFICATION:
        if not (cf.APP_TOKEN and cf.TOPICIDS):
            print("需要填写APP_TOKEN和TOPICIDS")


        data = {
                "appToken": cf.APP_TOKEN,
                "summary": summary,
                "content": message,
                "contentType": 1,
                "topicIds": [cf.TOPICIDS],
                "url": "",
                "verifyPay": False
                }
        ret = requests.post(url="https://wxpusher.zjiecode.com/api/send/message",
                      json=data)
        print(ret.content.decode())


if __name__ == '__main__':
    notification_pusher(summary="test",message="test content")
