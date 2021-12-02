import page


class HomeTeamListHandle(page.HomeTeamListPage):

    def switch_home_team_list_frame(self):
        self.driver.switch_to.frame(self.get_home_team_list_frame())

    def tap_view_team(self):
        self.execute_tap(self.get_team_view_ele())