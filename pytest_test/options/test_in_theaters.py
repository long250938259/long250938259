import requests
import json
import pytest
import os
from pytest_test.options.options_common import tranfer_common


@pytest.mark.transfer
class TestClass(tranfer_common):

    @pytest.mark.critical
    def test_001(self):
        settings_msg_before_transfer = "fdsfdsfds1232454~~~22~~~~~~~~~~但是分的高分1111233311"
        self.ome(settings=settings_msg_before_transfer)

    def test_002(self):
        s = "~~~3453~~~2343563~~~~"
        self.omea(settingsa=s)


if __name__ == '__main__':
    pytest.main("-r", "test_in_theaters")