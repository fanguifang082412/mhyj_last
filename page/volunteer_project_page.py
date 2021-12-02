from selenium.webdriver.common.by import By
import base


class VolunteerProjectPage(base.ActionElement):
    volunteer_project_feature = By.XPATH, '//*[@id="side-menu"]/li[3]/ul/li[2]/a'
    create_project_frame = By.XPATH, '//*[@id="content-main"]/iframe[2]'
    project_status_feature = By.XPATH, '//*[@id="app"]/div/div/form/div[2]/div/div/div/input'
    project_status_confirm = By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[4]/span'
    project_status_select = By.XPATH, '//*[@id="app"]/div/div/form/div[5]/div/button'
    create_activity_feature = By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/button[1]/span'

    def get_volunteer_project_ele(self):
        return self.get_element(self.volunteer_project_feature)

    def get_create_project_frame(self):
        return self.get_element(self.create_project_frame)

    def get_project_status_ele(self):
        return self.get_element(self.project_status_feature)

    def get_project_status_confirm_ele(self):
        return self.get_element(self.project_status_confirm)

    def get_project_status_select_ele(self):
        return self.get_element(self.project_status_select)

    def get_create_activity_ele(self):
        return self.get_element(self.create_activity_feature)




