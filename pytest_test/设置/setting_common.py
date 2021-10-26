from ks_login.ksp_api import TransferApi
from ks_login import load_log

log = load_log.Log()


class setting_common(object):

    user_api = TransferApi()

    def set_pre(self, settingsa):
        self.user_api.edit_my_front(settings_robot_prefix=settingsa)

    def question_key_word_search_hits1(self, shop_id, keyword):
        res = self.user_api.question_key_word_search_method(shop_id=shop_id, keyword=keyword)
        log.info(res)
        assert res["code"] == 0