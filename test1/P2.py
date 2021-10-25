# import requests
# import pprint
# import json
#
# data = {
#     "requestId": "303fe1ca-9d76-45e3-ac3e-41f6aa35a994",
#     "createTime": 0,
#     "generator": 1,
#     "type": 1,
#     "fromUser": {
#         "nickName": "在于自己",
#         "role": 1,
#         "openId": "Vb2oGFTksn5jWZZQiM8zqEl7Ox3pValH3Jw878iDQab"
#     },
#     "toUser": {
#         "nickName": "我是卖家呀呀呀呀呀！！！！！",
#         "role": 2
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
#         "content": "{\"text\":\"我考虑一下\"}"
#     }
# }
#
# url = "https://wangcai-test-ks.xiaoduoai.com/spi/chatbotevent"
#
# res = requests
# res1 = res.post(url=url, json=data )
# print(res1)
#
from ks_login import load_log
import time
from ks_login import mysql_support


mysql = mysql_support.MysqlDataGet()


log = load_log.Log()
log.debug("我是debug日志1111")
log.info('我是info日志111')
log.error('我是error日志11')
log.warning('我是warning日志1')

# mysql.write_log('日志','info','自动化测试','3333~~~')


# print(time.strftime('%Y-%m-%d %H:%M:%S'))











