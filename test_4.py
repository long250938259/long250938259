from locust import HttpUser, task, TaskSet, events, constant
import time, sys
import os

class UserBehavior(HttpUser):

    @task(1)
    def test_get(self):
        data = {
            "requestId": "303fe1ca-9d76-45e3-ac3e-41f6aa35a994",
            "createTime": 0,
            "generator": 1,
            "type": 1,
            "fromUser": {
                "nickName": "shilidia122222",
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
                "content": "{\"text\":\"包装太差\"}"
            }
        }
        print(111111111111111111)
        url = "https://wangcai-test-ks.xiaoduoai.com/spi/chatbotevent"
        res = self.client.post(url=url, json=data)
        print(res.json())


class WebUser(TaskSet):
    """性能测试配置 换算配置"""
    host = ""
    tasks = [UserBehavior]
    wait_time = constant(1)


if __name__ == '__main__':
    os.system('locust -f ./test_4.py -u 20 -r 1 --host https://wangcai-test-ks.xiaoduoai.com/ --web-host=127.0.0.1') # 试试
