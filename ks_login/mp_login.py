import requests
import json

class ApiLogin(object):
    def __init__(self):
        self.target_url = "https://wangcai-test-ks.xiaoduoai.com"
        self.online_login_url = "/api/xuanzang/mp_switcher"
        self.login_url = "/api/auth/mp_switcher"

    def login(self, company_name):
        url = self.target_url + self.login_url + "?subnick=" + company_name
        res = requests.get(url)
        json_res = json.loads(res.text)
        url_res = json_res['v4_url']
        res_login = requests.get(url_res)
        cookie_data = res_login.request.headers._store['cookie']
        return res_login, cookie_data[1]

if __name__ == "__main__":
    login = ApiLogin()
    headers = login.login(company_name="1901625824")
    print(headers)




