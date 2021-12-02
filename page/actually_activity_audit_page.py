from selenium.webdriver.common.by import By
import base



class ActuallyActivityAuditPage(base.ActionElement):

    activity_audit_pass_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/span/button[3]/span'
    activity_audit_fail_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/span/button[1]/span'
    activity_audit_fail_reason_feature = By.XPATH, '/html/body/div[3]/div/div[2]/form/div/div/div/textarea'
    activity_audit_fail_confirm_feature = By.XPATH, '/html/body/div[3]/div/div[3]/span/button[2]/span'
    activity_audit_reject_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/span/button[2]'
    activity_audit_reject_reason_feature = By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/input'
    activity_audit_reject_confirm_feature = By.XPATH, '/html/body/div[3]/div/div[3]/button[2]/span'

    def get_activity_audit_pass_ele(self):
        return self.get_element(self.activity_audit_pass_feature)

    def get_activity_audit_fail_ele(self):
        return self.get_element(self.activity_audit_fail_feature)

    def get_activity_audit_fail_reason_ele(self):
        return self.get_element(self.activity_audit_fail_reason_feature)

    def get_activity_audit_fail_confirm_ele(self):
        return self.get_element(self.activity_audit_fail_confirm_feature)

    def get_activity_audit_reject_ele(self):
        return self.get_element(self.activity_audit_reject_feature)

    def get_activity_audit_reject_reason_ele(self):
        return self.get_element(self.activity_audit_reject_reason_feature)

    def get_activity_audit_reject_confirm_ele(self):
        return self.get_element(self.activity_audit_reject_confirm_feature)



