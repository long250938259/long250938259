import requests
import json
from ks_login import mp_login
from ks_login import load_log

log = load_log.Log()

login1 = mp_login.ApiLogin()
headers = login1.login(company_name="1901625824")


class TransferApi(object):

    def __init__(self):
        self.target_url = "https://ks4.xiaoduoai.com"
        self.admin_xdservice_edit_my = "/api/admin/xdservice/edit_my"
        self.admin_config2_add_shop_transfer_v2 = "/api/admin/config2/add_shop_transfer/v2"
        self.condition_reply_admin_shop_search_global_cond_search = "/api/condition_reply_admin/shop/search/global/cond_answer" #条件搜索
        self.shop_setup_url = '/api/admin/guide/shop_setup'

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

    def question_key_word_search_method(self, shop_id, keyword):
        url = self.target_url + self.condition_reply_admin_shop_search_global_cond_search
        global_search_related = {
            "keyword": keyword,
            "main_type": "question",
            "question_type": ""

        }
        data = {
            "global_search_related": global_search_related,
            "shop_id": shop_id
        }
        json_data = {
            "global_search_related": {
                "main_type": "question",
                "question_type": "question_b",
                "keyword": keyword
            }
        }
        res = requests.post(url=url, json=json_data, headers=headers)
        log.info(res)
        json_res = json.loads(res.text)
        print(json_res)
        return json_res

    def set_shop_setup(self, category_id):
        url = self.target_url + self.shop_setup_url
        data = {
            'category_id': category_id
        }
        res = requests.post(url=url, json=data, headers=headers)
        log.info(res)
        json_res = json.loads(res.text)
        print(json_res)
        return json_res



# if __name__ == "__main__":
#     login = mp_login.ApiLogin()
#     headers = login.login(company_name="1901625824")
#     a = TransferApi()
#
#     a.edit_my_tranfer(settings_msg_before_transfer="fdsfdsfds1232454~~~~~~~~~~~1~~但是分的高分")


