from selenium.webdriver.common.by import By

import base


class PageLogin(base.ActionElement):
    username_feature = By.XPATH, "/html/body/div/form/div[1]/input"
    pwd_feature = By.XPATH, "/html/body/div/form/div[2]/input"
    login_feature = By.XPATH, "/html/body/div/form/button"

    def get_username_ele(self):
        return self.get_element(self.username_feature)

    def get_pwd_ele(self):
        return self.get_element(self.pwd_feature)

    def get_login_ele(self):
        return self.get_element(self.login_feature)



