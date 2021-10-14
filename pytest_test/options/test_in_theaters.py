import requests
import json
import pytest
import allure
import os
from pytest_test.options.options_common import tranfer_common
shop_id = "5ec76879edbe97000f8d850c"

@allure.epic("epic_platform")
@allure.feature('设置')
@allure.story('辅助面板设置')
@pytest.mark.transfer
class TestClass(tranfer_common):

    @allure.title('获取所有问题列表')
    @pytest.mark.critical
    @allure.severity('critical')
    def test_001(self):
        settings_msg_before_transfer = "我是转接的话术呀~~~1"
        self.ome(settings=settings_msg_before_transfer)



    @allure.title('搜索问题')
    @pytest.mark.critical
    @allure.severity('critical')
    def test_002(self):
        keyword = "你好"
        self.question_key_word_search_hits(shop_id=shop_id, keyword=keyword)

    #
    # @allure.title('获取所有问题列表1')
    # @pytest.mark.critical
    # @allure.severity('critical')
    # def test_002(self):
    #     s = "~~1~~"
    #     self.omea(settingsa=s)
    #
    # def test_003(self):
    #     shop_id = "5ec76879edbe97000f8d850c"
    #     question_id = "504820385"
    #     self.add_shop_tranfer(shop_id=shop_id, questions_ids=question_id)


# if __name__ == '__main__':
#     pytest.main()
    # pytest.main(['--alluredir', 'D:/ll/dj/long250938259/pytest_test/report'])
    # allure转换成---html并打开测试报告
    # os.system('cd D:/ll/dj/long250938259/pytest_test')
    # 清理上次的报告并生成新的报告
    # os.system('allure generate D:/ll/dj/long250938259/pytest_test/report -o D:/ll/dj/long250938259/pytest_test//report/html --clean')
    # os.system('allure serve D:/ll/dj/long250938259/pytest_test/report')
