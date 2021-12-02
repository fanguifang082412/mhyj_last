import time
pytest
from selenium.webdriver.common.by import By
import handle
import base
from business.test_add_team_business import TestAddTeam


class TestAuditTeam:

    def setup_class(self):
        self.driver = base.DriverUntil.get_driver()
        self.total_handle = handle.TotalHandle(self.driver)
        self.driver.get("http://47.102.168.233:8880/")
        self.total_handle.init_login().go_login("admin", "123456")

    def teardown_class(self):
        base.DriverUntil.quit_driver()

    def setup(self):
        self.driver.get("http://47.102.168.233:8880/")

    def audit_team_step(self):
        self.total_handle.init_home().switch_home_frame()
        time.sleep(1)
        self.total_handle.init_home().tap_audit_team()
        self.driver.switch_to.default_content()
        self.total_handle.init_home_team_list().switch_home_team_list_frame()
        self.total_handle.init_home_team_list().tap_view_team()
        self.driver.switch_to.default_content()
        self.total_handle.init_home_team_details().switch_home_team_details_frame()

    @pytest.mark.skip()
    def test_audit_team_pass(self):
        self.audit_team_step()
        self.total_handle.init_home_team_details().tap_team_audit_pass()
        self.total_handle.init_home_team_details().tap_audit_pass_confirm()
        self.total_handle.init_home_team_details().tap_audit_pass_last_confirm()
        assert_ele_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div/div[3]/span[2]'
        time.sleep(1)
        assert_ele = self.total_handle.init_home_team_details().get_element(assert_ele_feature)
        assert True if assert_ele.text == "组建完成" else False

    def test_audit_team_fail(self):
        self.audit_team_step()
        self.total_handle.init_home_team_details().tap_team_audit_fail()
        self.total_handle.init_home_team_details().input_audit_fail_reason("审核失败")
        self.total_handle.init_home_team_details().tap_audit_fail_confirm()
        assert_ele_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div/div[3]/span[2]'
        time.sleep(1)
        assert_ele = self.total_handle.init_home_team_details().get_element(assert_ele_feature)
        assert True if assert_ele.text == "组建失败" else False







