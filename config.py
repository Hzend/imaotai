ITEM_MAP = {
    "10213": "53%vol 500ml贵州茅台酒（癸卯兔年）",
    "10214": "53%vol 375ml×2贵州茅台酒（癸卯兔年）",
    "10056": "53%vol 500ml茅台1935",
    "2478": "53%vol 500ml贵州茅台酒（珍品）"
}

# 需要预约的商品(默认只预约2个兔茅)
########################
ITEM_CODES = ['10213', '10214']

# push plus 微信推送,具体使用参考  https://www.pushplus.plus
# 例如： PUSH_TOKEN = '123456'
########################
# 不填不推送消息，一对一发送
PUSH_TOKEN = None
########################
# 如需通过微信提醒，
# 1、在https://wxpusher.zjiecode.com/admin申请app_token；
# 2、将app_token和topic_ids填入下方，修改NOTIFICATION = True
WECHAT_NOTIFICATION = False
APP_TOKEN = ""
TOPIC_IDS = 0
########################

# credentials 路径，例如：CREDENTIALS_PATH = /home/user/.imoutai/credentials
# 不配置，使用默认路径，在宿主目录
# 例如： CREDENTIALS_PATH = '/home/user/.imautai/credentials'
########################
CREDENTIALS_PATH = None
########################

# 预约规则配置
########################
# 预约本市出货量最大的门店
MAX_ENABLED = True
# 预约你的位置附近门店
DISTANCE_ENABLED = False
########################
