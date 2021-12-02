import sys, os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

import base
import handle
import time
from selenium.webdriver.common.by import By


class TestActivityAudit:

    def setup_class(self):

        self.driver = base.DriverUntil.get_driver()
        self.total_handle = handle.TotalHandle(self.driver)
        self.driver.get("http://47.102.168.233:8880/")
        self.total_handle.init_login().go_login("admin", "123456")

    def teardown_class(self):
        base.DriverUntil.quit_driver()

    def setup(self):
        self.driver.get("http://47.102.168.233:8880/")

    def test_activity_audit_success(self):
        self.total_handle.init_home().tap_volunteer_service()
        time.sleep(1)
        self.total_handle.init_check_activity().tap_activity_check()
        self.total_handle.init_check_activity().switch_activity_check_frame()
        self.total_handle.init_check_activity().tap_activity_status()
        time.sleep(1)
        self.total_handle.init_check_activity().tap_activity_status_confirm()
        self.total_handle.init_check_activity().tap_activity_status_select()
        self.total_handle.init_check_activity().tap_activity_check_btn()
        self.total_handle.init_actually_activity().tap_activity_audit_pass()
        assert_ele_feature = By.XPATH, '/html/body/div[3]/p'
        time.sleep(1)
        assert_ele = self.driver.find_element(*assert_ele_feature)
        assert True if assert_ele.text == "审批通过" else False

    def test_activity_audit_fail(self):
        self.total_handle.init_home().tap_volunteer_service()
        time.sleep(1)
        self.total_handle.init_check_activity().tap_activity_check()
        self.total_handle.init_check_activity().switch_activity_check_frame()
        self.total_handle.init_check_activity().tap_activity_status()
        time.sleep(1)
        self.total_handle.init_check_activity().tap_activity_status_confirm()
        self.total_handle.init_check_activity().tap_activity_status_select()
        time.sleep(1)
        self.total_handle.init_check_activity().tap_activity_check_btn()
        self.total_handle.init_actually_activity().tap_activity_audit_fail()
        self.total_handle.init_actually_activity().input_activity_audit_fail_reason("测试不通过")
        self.total_handle.init_actually_activity().tap_activity_audit_fail_confirm()
        assert_ele_feature = By.XPATH, '/html/body/div[4]/p'
        time.sleep(1)
        assert_ele = self.driver.find_element(*assert_ele_feature)
        assert True if assert_ele.text == "处理成功!" else False

    def test_activity_audit_reject(self):
        self.total_handle.init_home().tap_volunteer_service()
        time.sleep(1)
        self.total_handle.init_check_activity().tap_activity_check()
        self.total_handle.init_check_activity().switch_activity_check_frame()
        self.total_handle.init_check_activity().tap_activity_status()
        time.sleep(1)
        self.total_handle.init_check_activity().tap_activity_status_confirm()
        self.total_handle.init_check_activity().tap_activity_status_select()
        time.sleep(1)
        self.total_handle.init_check_activity().tap_activity_check_btn()
        self.total_handle.init_actually_activity().tap_activity_audit_reject()
        self.total_handle.init_actually_activity().input_activity_audit_reject_reason("审核拒绝")
        self.total_handle.init_actually_activity().tap_activity_audit_reject_confirm()
        assert_ele = self.total_handle.init_check_activity().get_activity_check_btn_ele()
        assert True if "处理考勤" in assert_ele.text else False









