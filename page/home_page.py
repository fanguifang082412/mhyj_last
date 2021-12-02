from selenium.webdriver.common.by import By
import base


class HomePage(base.ActionElement):
    home_feature = By.XPATH, '//*[@id="side-menu"]/li[2]/a/span'
    volunteer_service = By.XPATH, '//*[@id="side-menu"]/li[3]/a/span[1]'
    home_frame_feature = By.XPATH, '//*[@id="content-main"]/iframe'
    audit_team_feature = By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div/button/span'

    def get_home_ele(self):
        return self.get_element(self.home_feature)

    def get_volunteer_service_ele(self):
        return self.get_element(self.volunteer_service)

    def get_home_frame(self):
        return self.get_element(self.home_frame_feature)

    def get_audit_team_ele(self):
        return self.get_element(self.audit_team_feature)