import requests

data = {
    "requestId": "303fe1ca-9d76-45e3-ac3e-41f6aa35a994",
    "createTime": 0,
    "generator": 1,
    "type": 1,
    "fromUser": {
        "nickName": "在于自己",
        "role": 1,
        "openId": "Vb2oGFTksn5jWZZQiM8zqEl7Ox3pValH3Jw878iDQab"
    },
    "toUser": {
        "nickName": "三里清风",
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
        "content": "{\"text\":\"32结婚2313xd\"}"
    }
}

url = "https://wangcai-test-ks.xiaoduoai.com/spi/chatbotevent"

res = requests
res1 = res.post(url=url, json=data )
print(res1.json())






















