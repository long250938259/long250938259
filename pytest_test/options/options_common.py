import requests
from ks_login.ksp_api import TransferApi


class tranfer_common(object):

    tranfer = TransferApi()

    def ome(self, settings):
        self.tranfer.edit_my_tranfer(settings_msg_before_transfer=settings)

    def omea(self, settingsa):
        self.tranfer.edit_my_front(settings_robot_prefix=settingsa)

    def add_shop_tranfer(self, shop_id, questions_ids):
        res = self.tranfer.add_shop_tranfer_v2(shop_id=shop_id, questions_ids=questions_ids)
        assert res["code"] == 0
