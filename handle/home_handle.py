import page


class HomeHandle(page.HomePage):
    def tap_home(self):
        self.execute_tap(self.get_home_ele())

    def tap_volunteer_service(self):
        self.execute_tap(self.get_volunteer_service_ele())

    def switch_home_frame(self):
        self.driver.switch_to.frame(self.get_home_frame())

    def tap_audit_team(self):
        self.execute_tap(self.get_audit_team_ele())