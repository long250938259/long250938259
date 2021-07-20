import requests
import json
import pytest
from pytest_test.options.options_common import tranfer_common


@pytest.mark.transfer
class TestTranfer(tranfer_common):

    @pytest.mark.critical
    def test_001(self):
        settings_msg_before_transfer = "fdsfdsfds1232454~~~~~~~~~~~~~但是分的高分1111233311"
        self.ome(settings=settings_msg_before_transfer)


