import pytest
import allure
import os
from pytest_test.设置.setting_common import setting_common
shop_id = "5ec76879edbe97000f8d850c"


@allure.epic("epic_platform1")
@allure.feature('设置')
@allure.story('辅助面板设置')
@pytest.mark.transfer
class TestClass(setting_common):

    @allure.title('设置回复前缀')
    @pytest.mark.critical
    @allure.severity('critical')
    def test_0001(self):
        s = "回复前缀~~~~~~~~~~~"
        self.set_pre(settingsa=s)