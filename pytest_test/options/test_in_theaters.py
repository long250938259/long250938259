import requests
import json
import pytest
from ks_login.ksp_api import TransferApi


@pytest.mark.transfer
class TestTranfer(TransferApi):

    @pytest.mark.critical
    def test_001(self):
        settings_msg_before_transfer = "fdsfdsfds1232454~~~~~~~~~~~~~但是分的高分1111233311"
        self.edit_my_tranfer(settings_msg_before_transfer=settings_msg_before_transfer)

#
# if __name__ == "__main__":
#     a = TestTranfer()
#     a.test001()


