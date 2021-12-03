import time
import sys, os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from base import ActionElement
import pytest
from selenium.webdriver.common.by import By
import handle
import base




class TestAddTeam:

    def setup_class(self):

        self.driver = base.DriverUntil.get_driver()
        self.total_handle = handle.TotalHandle(self.driver)
        self.driver.get("http://47.102.168.233:8880/")
        self.total_handle.init_login().go_login("admin", "123456")

    def setup(self):
        self.driver.get("http://47.102.168.233:8880/")

    def teardown_class(self):
        base.DriverUntil.quit_driver()

    def add_team_step(self, info):
        self.total_handle.init_home().tap_volunteer_service()
        time.sleep(1)
        self.total_handle.init_volunteer_team().tap_volunteer_team()
        self.total_handle.init_volunteer_team().switch_create_team_frame()
        self.total_handle.init_volunteer_team().tap_create_team()
        self.total_handle.init_add_team().input_team_name(info["team_name"])
        self.total_handle.init_add_team().input_team_total_name(info["team_total_name"])
        self.total_handle.init_add_team().input_team_image(info["team_image"])
        self.total_handle.init_add_team().input_team_creater(info["team_creater"])
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_yunying()
        time.sleep(1)
        self.total_handle.init_add_team().input_team_yunying(info["team_yunying"])
        self.total_handle.init_add_team().tap_team_yunying_select()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_yunying_choose()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_date()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_date_confirm()
        self.total_handle.init_add_team().tap_team_province()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_province_confirm()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_shi()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_shi_confirm()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_qu()
        time.sleep(2)
        self.total_handle.init_add_team().tap_team_qu_confirm()
        self.total_handle.init_add_team().input_team_office_address(info["team_office_address"])
        self.total_handle.init_add_team().input_team_connecter(info["team_connecter"])
        self.total_handle.init_add_team().input_team_phone(info["team_phone"])
        self.total_handle.init_add_team().tap_team_service()
        self.total_handle.init_add_team().input_team_introduce(info["team_introduce"])
        self.total_handle.init_add_team().tap_team_create_btn()

    @pytest.mark.parametrize("info", ActionElement.get_data("add_team_data", "add_team_success") )
    def test_add_team_success(self, info):
        self.add_team_step(info)
        assert_ele_feature = By.XPATH, '/html/body/div[7]/p'
        assert_ele = self.total_handle.init_add_team().get_element(assert_ele_feature)
        assert_info = assert_ele.text
        assert True if assert_info == info["assert_info"] else False

    @pytest.mark.parametrize("info", ActionElement.get_data("add_team_data", "add_team_fail"))
    def test_add_team_fail(self, info):
        self.add_team_step(info)
        assert_ele_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/span'
        assert_ele = self.driver.find_element(*assert_ele_feature)
        assert True if assert_ele else False

    @pytest.mark.parametrize("info", ActionElement.get_data("add_team_data", "add_team_url_null"))
    def test_add_team_url_null(self, info):
        self.total_handle.init_home().tap_volunteer_service()
        time.sleep(1)
        self.total_handle.init_volunteer_team().tap_volunteer_team()
        self.total_handle.init_volunteer_team().switch_create_team_frame()
        self.total_handle.init_volunteer_team().tap_create_team()
        self.total_handle.init_add_team().input_team_name(info["team_name"])
        self.total_handle.init_add_team().input_team_total_name(info["team_total_name"])
        self.total_handle.init_add_team().input_team_creater(info["team_creater"])
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_yunying()
        time.sleep(1)
        self.total_handle.init_add_team().input_team_yunying(info["team_yunying"])
        self.total_handle.init_add_team().tap_team_yunying_select()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_yunying_choose()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_date()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_date_confirm()
        self.total_handle.init_add_team().tap_team_province()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_province_confirm()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_shi()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_shi_confirm()
        time.sleep(1)
        self.total_handle.init_add_team().tap_team_qu()
        time.sleep(2)
        self.total_handle.init_add_team().tap_team_qu_confirm()
        self.total_handle.init_add_team().input_team_office_address(info["team_office_address"])
        self.total_handle.init_add_team().input_team_connecter(info["team_connecter"])
        self.total_handle.init_add_team().input_team_phone(info["team_phone"])
        self.total_handle.init_add_team().tap_team_service()
        self.total_handle.init_add_team().input_team_introduce(info["team_introduce"])
        self.total_handle.init_add_team().tap_team_create_btn()
        assert_ele_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/span'
        assert_ele = self.driver.find_element(*assert_ele_feature)
        assert True if assert_ele else False






