# import requests

import base64

# data = {
#     "requestId": "303fe1ca-9d76-45e3-ac3e-41f6aa35a994",
#     "createTime": 0,
#     "generator": 1,
#     "type": 1,
#     "fromUser": {
#         "nickName": "在于自己",
#         "role": 1,
#         "openId": "Vb2oGFTksn5jWZZQiM8zqEl7Ox3pValH3Jw878iDQab01"
#     },
#     "toUser": {
#         "nickName": "哦里1",
#         "role": 3
#     },
#     # "transferList": None,
#     "context": {
#         "sellerId": 1901625824,
#         "itemId": 0,
#         "orderId": 0,
#         "orderStatus": 0,
#         "assistantOnlineStatus": 0
#     },
#     "message": {
#         "contentType": 1,
#         "content": "{\"text\":\"那算了\"}"
#     }
# }
#
# url = "https://wangcai-test-ks.xiaoduoai.com/spi/chatbotevent"
#
# res = requests
# res1 = res.post(url=url, json=data )
# print(res1.json())

# !/usr/bin/python3

# def encryption(st):
#     encode1 = base64.b64encode(st.encode('utf-8'))
#     return str(encode1, 'utf-8')
#
#
# def decrypt(st):
#     decode1 = base64.b64decode(st)
#     return str(decode1, 'utf-8')
#
#
# a = encryption("lilong")
# print(a)
# b = decrypt(a)
# print(b)
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
print(curPath)
print(rootPath)