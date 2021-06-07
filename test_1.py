import requests
import pprint
import json

data = {
    "requestId": "303fe1ca-9d76-45e3-ac3e-41f6aa35a994",
    "createTime": 0,
    "generator": 1,
    "type": 1,
    "fromUser": {
        "nickName": "我是买家啊啊啊1122244211",
        "role": 1,
        "openId": "2m4JPAGoC0cV0xYkWSiGZv1jQkdZkAnRjRSU0qH9L1t001"
    },
    "toUser": {
        "nickName": "我是卖家呀呀呀",
        "role": 2
    },
    # "transferList": None,
    "context": {
        "sellerId": 1901625824,
        "itemId": 0,
        "orderId": 0,
        "orderStatus": 0,
        "assistantOnlineStatus": 0
    },
    "message": {
        "contentType": 1,
        "content": "{\"text\":\"473598402sddsf\"}"
    }
}

url = "https://wangcai-test-ks.xiaoduoai.com/spi/chatbotevent"

res = requests
res1 = res.post(url=url, json=data )
print(res1.json())






















