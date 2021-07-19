import requests

data = {
    "requestId": "303fe1ca-9d76-45e3-ac3e-41f6aa35a994",
    "createTime": 0,
    "generator": 1,
    "type": 1,
    "fromUser": {
        "nickName": "shilidian1",
        "role": 1,
        "openId": "nntOEKMDKwm1Qk6Tevy8GHgGa2ZtWg5t12f0irch1121"
    },
    "toUser": {
        "nickName": "wufei",
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
        "content": "{\"text\":\"寄回的商品显示已签收\"}"
    }
}

url = "https://wangcai-test-ks.xiaoduoai.com/spi/chatbotevent"

res = requests
res1 = res.post(url=url, json=data )
print(res1.json())






















