from selenium.webdriver.common.by import By
import base


class ActivityCheckPage(base.ActionElement):

    activity_check_feature = By.XPATH, '//*[@id="side-menu"]/li[3]/ul/li[5]/a'
    activity_status_feature = By.XPATH, '//*[@id="app"]/form/div[2]/div/div/div/input'
    activity_status_confirm_feature = By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[3]'
    activity_status_select_feature = By.XPATH, '//*[@id="app"]/form/div[5]/div/button/span'
    activity_check_btn_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/button/span'
    activity_check_frame_feature = By.XPATH, '//*[@id="content-main"]/iframe[2]'

    def get_activity_check_ele(self):
        return self.get_element(self.activity_check_feature)

    def get_activity_status_ele(self):
        return self.get_element(self.activity_status_feature)

    def get_activity_status_confirm_ele(self):
        return self.get_element(self.activity_status_confirm_feature)

    def get_activity_status_select_ele(self):
        return self.get_element(self.activity_status_select_feature)

    def get_activity_check_btn_ele(self):
        return self.get_element(self.activity_check_btn_feature)

    def get_activity_check_frame(self):
        return self.get_element(self.activity_check_frame_feature)
