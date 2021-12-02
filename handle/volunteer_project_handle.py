import page


class VolunteerProjectHandle(page.VolunteerProjectPage):

    def tap_volunteer_project(self):
        self.execute_tap(self.get_volunteer_project_ele())

    def switch_create_project_frame(self):
        self.driver.switch_to.frame(self.get_create_project_frame())

    def tap_project_status(self):
        self.execute_tap(self.get_project_status_ele())

    def tap_project_status_confirm(self):
        self.execute_tap(self.get_project_status_confirm_ele())

    def tap_project_status_select(self):
        self.execute_tap(self.get_project_status_select_ele())

    def tap_create_activity(self):
        self.execute_tap(self.get_create_activity_ele())