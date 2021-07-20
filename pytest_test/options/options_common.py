import requests
from ks_login.ksp_api import TransferApi


class tranfer_common(TransferApi):
    def ome(self, settings):
        self.edit_my_tranfer(settings_msg_before_transfer=settings)