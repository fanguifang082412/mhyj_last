import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import handle
import base


class TestCreateActivity:

    def setup_class(self):
        self.driver = base.DriverUntil.get_driver()
        self.total_handle = handle.TotalHandle(self.driver)

    def teardown_class(self):
        base.DriverUntil.quit_driver()

    def setup(self):
        self.driver.get("http://47.102.168.233:8880/")
        self.total_handle.init_login().go_login("admin", "123456")

    def add_activity_step(self):
        self.total_handle.init_home().tap_volunteer_service()
        time.sleep(1)
        self.total_handle.init_volunteer_project().tap_volunteer_project()
        self.total_handle.init_volunteer_project().switch_create_project_frame()
        self.total_handle.init_volunteer_project().tap_project_status()
        time.sleep(1)
        self.total_handle.init_volunteer_project().tap_project_status_confirm()
        self.total_handle.init_volunteer_project().tap_project_status_select()
        time.sleep(1)
        self.total_handle.init_volunteer_project().tap_create_activity()
        self.driver.switch_to.default_content()
        self.total_handle.init_create_activity().switch_create_activity_frame()
        self.total_handle.init_create_activity().tap_volunteer_team()
        self.total_handle.init_create_activity().input_volunteer_team("团队")
        self.total_handle.init_create_activity().tap_volunteer_team_select()
        self.total_handle.init_create_activity().tap_activity_volunteer_team()
        self.total_handle.init_create_activity().tap_activity_volunteer_team_confirm()
        self.total_handle.init_create_activity().input_activity_participants("10")
        self.total_handle.init_create_activity().input_activity_name("测试活动名称")
        time.sleep(1)
        self.total_handle.init_create_activity().tap_activity_start_time()
        time.sleep(1)
        self.total_handle.init_create_activity().tap_activity_start_time_confirm()
        time.sleep(1)
        self.total_handle.init_create_activity().tap_activity_end_time()
        time.sleep(1)
        js = "window.scrollTo(0,1000)"
        self.driver.execute_script(js)
        self.total_handle.init_create_activity().tap_activity_end_time_confirm()
        self.total_handle.init_create_activity().input_activity_address("广州")
        time.sleep(1)
        self.total_handle.init_create_activity().tap_activity_address_confirm()
        time.sleep(1)
        self.total_handle.init_create_activity().input_activity_detail_address("广州")
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(0, 200).click().perform()
        time.sleep(1)
        self.total_handle.init_create_activity().tap_create_activity_btn()
        self.driver.switch_to.default_content()
        assert_frame_feature = By.XPATH, '//*[@id="content-main"]/iframe[3]'
        assert_frame_ele = self.total_handle.init_create_activity().get_element(assert_frame_feature)
        self.driver.switch_to.frame(assert_frame_ele)
        assert_ele_feature = By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[1]/div[1]/div/span'
        assert_ele = self.total_handle.init_create_activity().get_element(assert_ele_feature)
        assert True if assert_ele.text == "活动创建成功" else False

    def test_create_activity(self):
        self.add_activity_step()



