import page


class HomeTeamDetailsHandle(page.HomeTeamDetailsPage):

    def switch_home_team_details_frame(self):
        self.driver.switch_to.frame(self.get_home_team_details_frame())

    def tap_team_audit_pass(self):
        self.execute_tap(self.get_audit_pass_ele())

    def tap_team_audit_fail(self):
        self.execute_tap(self.get_audit_fail_ele())

    def tap_audit_pass_confirm(self):
        self.execute_tap(self.get_audit_pass_confirm_ele())

    def tap_audit_pass_last_confirm(self):
        self.execute_tap(self.get_audit_pass_last_confirm_ele())

    def input_audit_fail_reason(self, fail_reason):
        self.execute_input(self.get_audit_fail_reason_ele(), fail_reason)

    def tap_audit_fail_confirm(self):
        self.execute_tap(self.get_audit_fail_confirm_ele())