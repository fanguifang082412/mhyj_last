from selenium.webdriver.common.by import By
import base


class VolunteerTeamPage(base.ActionElement):

    volunteer_team_feature = By.XPATH, '//*[@id="side-menu"]/li[3]/ul/li[3]/a'
    create_team_iframe = By.XPATH, '//*[@id="content-main"]/iframe[2]'
    create_team_feature = By.XPATH, '//*[@id="app"]/form/div[5]/div/button/span'

    def get_volunteer_team_ele(self):
        return self.get_element(self.volunteer_team_feature)

    def get_create_team_iframe(self):
        return self.get_element(self.create_team_iframe)

    def get_create_team_ele(self):
        return self.get_element(self.create_team_feature)



