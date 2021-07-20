import requests
from ks_login.ksp_api import TransferApi


class tranfer_common(object):

    tranfer = TransferApi()

    def ome(self, settings):
        self.tranfer.edit_my_tranfer(settings_msg_before_transfer=settings)

    def omea(self, settingsa):
        self.tranfer.edit_my_front(settings_robot_prefix=settingsa)
