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
        self.condition_reply_admin_shop_search_global_cond_search = "/api/condition_reply_admin/shop/search/global/cond_answer"

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
            },
            "common_search_related": {
                "sale_statuses": ["1.*", "1.1001", "1.1002", "1.1003", "2.*", "2.2001", "3.*", "3.3001", "3.3002",
                                  "4.*", "4.4001", "4.4002", "4.4003", "4.4004", "4.4005", "4.4006", "4.4007", "4.4008",
                                  "4.4009"],
                "ageing": [""],
                "hybrid_auto_send": 0,
                "full_auto_send": 0,
                "reply_sequence": 0,
                "customer_group": [],
                "goods_attribute": [],
                "vars": []
            },
            "goods_related": {
                "associated_with_goods": 0,
                "onsale": False,
                "goods_id": []
            },
            "goods_category_related": {
                "associated_with_goods_category": 0,
                "goods_category_ids": []
            },
            "precise_intent_related": {
                "associated_with_precise_intent": 0,
                "precise_intent_name": "",
                "precise_intent_keyword": ""
            },
            "question_related": {
                "is_rhetorical": 0
            },
            "show_realted": {
                "skip": 0,
                "limit": 20,
                "sort_by": ""
            },
            "shop_id": shop_id
        }
        res = requests.post(url=url, json=json_data, headers=headers)
        json_res = json.loads(res.text)
        print(json_res)
        return json_res



# if __name__ == "__main__":
#     login = mp_login.ApiLogin()
#     headers = login.login(company_name="1901625824")
#     a = TransferApi()
#
#     a.edit_my_tranfer(settings_msg_before_transfer="fdsfdsfds1232454~~~~~~~~~~~1~~但是分的高分")


