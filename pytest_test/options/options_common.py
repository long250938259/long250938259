import requests
from ks_login.ksp_api import TransferApi
from ks_login import load_log

log = load_log.Log()


class tranfer_common(object):

    tranfer = TransferApi()

    def ome(self, settings):
        self.tranfer.edit_my_tranfer(settings_msg_before_transfer=settings)

    def omea(self, settingsa):
        self.tranfer.edit_my_front(settings_robot_prefix=settingsa)

    def add_shop_tranfer(self, shop_id, questions_ids):
        res = self.tranfer.add_shop_tranfer_v2(shop_id=shop_id, questions_ids=questions_ids)
        assert res["code"] == 0

    def question_key_word_search_hits(self, shop_id, keyword):
        res = self.tranfer.question_key_word_search_method(shop_id=shop_id, keyword=keyword)
        log.info(res)
        assert res["code"] == 0
