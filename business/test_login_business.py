import sys, os
import time
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
import pytest
from selenium.webdriver.common.by import By
import handle
import base




class TestLoginBusiness:

    def setup_class(self):

        self.driver = base.DriverUntil.get_driver()
        self.total_handles = handle.TotalHandle(self.driver)

    def teardown_class(self):
        base.DriverUntil.quit_driver()

    def setup(self):
        self.driver.get("http://47.102.168.233:8880/")

    @pytest.mark.parametrize("test_data", base.ActionElement.get_data("login_data", "login_error"))
    def test_login_error(self, test_data):
        self.total_handles.init_login().input_username(test_data["username"])
        self.total_handles.init_login().input_pwd(test_data["password"])
        self.total_handles.init_login().tap_login_btn()
        assert_login_ele = self.total_handles.init_login().get_login_ele()
        assert True if assert_login_ele else False

    @pytest.mark.parametrize("test_data", base.ActionElement.get_data("login_data", "login_success"))
    def test_login_success(self, test_data):
        self.total_handles.init_login().input_username(test_data["username"])
        self.total_handles.init_login().input_pwd(test_data["password"])
        self.total_handles.init_login().tap_login_btn()
        time.sleep(1)
        assert_feature = By.XPATH, '//*[@id="page-wrapper"]/div[2]/a'
        assert_ele = self.total_handles.init_login().get_element(assert_feature)
        assert True if assert_ele else False






