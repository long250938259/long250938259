import requests
import json
import configparser
import os

config = configparser.ConfigParser()
project_path = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
config_path = os.path.join(os.path.join(project_path, 'config'), "config.ini")
config.read(config_path, encoding="utf-8")


class ApiLogin(object):
    def __init__(self):
        self.target_url = config.get("ProjectConfig", 'target_url')
        self.online_login_url = config.get("ProjectConfig", 'online_login_url')
        self.login_url = config.get("ProjectConfig", 'login_url')

    def login(self, company_name):
        url = self.target_url + self.login_url + "?subnick=" + company_name
        res = requests.get(url)
        json_res = json.loads(res.text)
        url_res = json_res['v4_url']
        res_login = requests.get(url_res)
        cookie_data = res_login.request.headers._store['cookie']
        headers = {
            "Xiaoduo-Platform": "ks",
            "Cookie": cookie_data[1]
        }
        return headers

# if __name__ == "__main__":
#     login = ApiLogin()
#     headers = login.login(company_name="1901625824")
#     print(headers)




