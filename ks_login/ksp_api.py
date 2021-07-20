import requests
import json
from ks_login import mp_login

log = mp_login.ApiLogin()
headers = log.login(company_name="1901625824")


class TransferApi(object):

    def __init__(self):
        self.target_url = "https://wangcai-test-ks.xiaoduoai.com"
        self.admin_xdservice_edit_my = "/api/admin/xdservice/edit_my"

    def edit_my_tranfer(self, settings_msg_before_transfer):
        url = self.target_url + self.admin_xdservice_edit_my
        data = {
            "settings_msg_before_transfer": settings_msg_before_transfer
        }
        res = requests.post(url=url, data=data, headers=headers)
        json_res = json.loads(res.text)
        print(json_res)


# if __name__ == "__main__":
#     login = mp_login.ApiLogin()
#     headers = login.login(company_name="1901625824")
#     a = TransferApi()
#
#     a.edit_my_tranfer(settings_msg_before_transfer="fdsfdsfds1232454~~~~~~~~~~~1~~但是分的高分")


