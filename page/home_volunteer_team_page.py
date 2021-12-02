from selenium.webdriver.common.by import By
import base


class HomeTeamListPage(base.ActionElement):

    home_team_list_frame_feature = By.XPATH, '//*[@id="content-main"]/iframe[2]'
    team_view_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/button[1]/span'

    def get_home_team_list_frame(self):
        return self.get_element(self.home_team_list_frame_feature)

    def get_team_view_ele(self):
        return self.get_element(self.team_view_feature)