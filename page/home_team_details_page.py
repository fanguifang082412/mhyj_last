from selenium.webdriver.common.by import By
import base


class HomeTeamDetailsPage(base.ActionElement):

    team_details_frame_feature = By.XPATH, '//*[@id="content-main"]/iframe[3]'
    audit_pass_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div/button[1]/span'
    audit_fail_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div/button[2]'
    audit_pass_confirm_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/button[2]/span'
    audit_pass_last_confirm_feature = By.XPATH, '/html/body/div[2]/div/div[3]/button[2]'
    audit_fail_reason_feature = By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/textarea'
    audit_fail_confirm_feature = By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span'

    def get_home_team_details_frame(self):
        return self.get_element(self.team_details_frame_feature)

    def get_audit_pass_ele(self):
        return self.get_element(self.audit_pass_feature)

    def get_audit_fail_ele(self):
        return self.get_element(self.audit_fail_feature)

    def get_audit_pass_confirm_ele(self):
        return self.get_element(self.audit_pass_confirm_feature)

    def get_audit_pass_last_confirm_ele(self):
        return self.get_element(self.audit_pass_last_confirm_feature)

    def get_audit_fail_reason_ele(self):
        return self.get_element(self.audit_fail_reason_feature)

    def get_audit_fail_confirm_ele(self):
        return self.get_element(self.audit_fail_confirm_feature)
