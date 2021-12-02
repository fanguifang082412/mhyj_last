import page



class VolunteerTeamHandle(page.VolunteerTeamPage):

    def tap_volunteer_team(self):
        self.execute_tap(self.get_volunteer_team_ele())

    def switch_create_team_frame(self):
        self.driver.switch_to.frame(self.get_create_team_iframe())

    def tap_create_team(self):
        self.execute_tap(self.get_create_team_ele())
