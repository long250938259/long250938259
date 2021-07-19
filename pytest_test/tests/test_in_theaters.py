import requests
import json


class TestInTheaters(object):
    def test_in_theater(self):
        host = "https://movie.douban.com"
        path = '/j/search_subjects'
        params = {
            "type": "movie",
            "tag": "热门",
            "page_limit": 50,
            "page_start": 0
        }
        headers = {
            "Cookie": "bid=ZJWqvp1f3CI"
        }
        r = requests.request("get", url=host+path, headers=headers, params=params)
        response = r.json()
        print(response)
        assert response["title"] == "正在上映的电影-上海"



