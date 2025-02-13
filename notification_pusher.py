import config as cf
import requests
import logging


def notification_pusher(summary: str, message: str):
    if cf.WECHAT_NOTIFICATION:
        if not (cf.APP_TOKEN and cf.TOPIC_IDS):
            logging.info("需要填写APP_TOKEN和TOPICIDS")
        data = {
            "appToken": cf.APP_TOKEN,
            "summary": summary,
            "content": message,
            "contentType": 1,
            "topicIds": [cf.TOPIC_IDS],
            "url": "",
            "verifyPay": False
        }
        try:
            ret = requests.post(url="https://wxpusher.zjiecode.com/api/send/message",
                                json=data)
            logging.info(f"{ret.content.decode()}")
        except Exception as e:
            logging.error(f"微信通知发生错误，错误原因{e}")


if __name__ == '__main__':
    notification_pusher(summary="test", message="test content")
