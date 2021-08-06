import requests
import json
from ks_login import mp_login

log = mp_login.ApiLogin()
headers = log.login(company_name="1901625824")


class TransferApi(object):

    def __init__(self):
        self.target_url = "https://ks4.xiaoduoai.com"
        self.admin_xdservice_edit_my = "/api/admin/xdservice/edit_my"
        self.admin_config2_add_shop_transfer_v2 = "/api/admin/config2/add_shop_transfer/v2"

    def edit_my_tranfer(self, settings_msg_before_transfer):
        url = self.target_url + self.admin_xdservice_edit_my
        data = {
            "settings_msg_before_transfer": settings_msg_before_transfer
        }
        res = requests.post(url=url, data=data, headers=headers)
        json_res = json.loads(res.text)
        print(json_res)

    def edit_my_front(self, settings_robot_prefix):
        url = self.target_url + self.admin_xdservice_edit_my
        data = {
            "settings_robot_prefix": settings_robot_prefix
        }
        res = requests.post(url=url, data=data, headers=headers)
        json_res = json.loads(res.text)
        print(json_res)

    def add_shop_tranfer_v2(self, shop_id, questions_ids):
        url = self.target_url + self.admin_config2_add_shop_transfer_v2
        data = {
            "shop_id": shop_id,
            "question_ids": questions_ids
        }
        res = requests.post(url=url, data=data, headers=headers, )
        json_res = json.loads(res.text)
        print(json_res)
        return json_res


# if __name__ == "__main__":
#     login = mp_login.ApiLogin()
#     headers = login.login(company_name="1901625824")
#     a = TransferApi()
#
#     a.edit_my_tranfer(settings_msg_before_transfer="fdsfdsfds1232454~~~~~~~~~~~1~~但是分的高分")


