import page


class CreateActivityHandle(page.CreateActivityPage):

    def switch_create_activity_frame(self):
        self.driver.switch_to.frame(self.get_create_activity_frame())

    def tap_volunteer_team(self):
        self.execute_tap(self.get_volunteer_team_ele())

    def input_volunteer_team(self, volunteer_team):
        self.execute_input(self.get_volunteer_team_input_ele(), volunteer_team)

    def tap_volunteer_team_select(self):
        self.execute_tap(self.get_volunteer_team_select_ele())

    def tap_activity_volunteer_team(self):
        self.execute_tap(self.get_activity_volunteer_team_ele())

    def tap_activity_volunteer_team_confirm(self):
        self.execute_tap(self.get_activity_volunteer_team_confirm_ele())

    def input_activity_participants(self, activity_participants):
        self.get_activity_participants_ele().clear()
        self.execute_input(self.get_activity_participants_ele(), activity_participants)

    def input_activity_name(self, activity_name):
        self.execute_input(self.get_activity_name_ele(), activity_name)

    def tap_activity_start_time(self):
        self.execute_tap(self.get_activity_start_time_ele())

    def tap_activity_start_time_confirm(self):
        self.execute_tap(self.get_activity_start_time_confirm_ele())

    def tap_activity_end_time(self):
        self.execute_tap(self.get_activity_end_time_ele())

    def tap_activity_end_time_confirm(self):
        self.execute_tap(self.get_activity_end_time_confirm_ele())

    def input_activity_address(self, activity_address):
        self.execute_input(self.get_activity_address_input_ele(), activity_address)

    def tap_activity_address_confirm(self):
        self.execute_tap(self.get_activity_address_confirm_ele())

    def input_activity_detail_address(self, activity_detail_address):
        self.execute_input(self.get_activity_detail_address_ele(), activity_detail_address)

    def tap_activity_coordinates_address(self):
        self.execute_tap(self.get_activity_coordinates_address_ele())

    def tap_create_activity_btn(self):
        self.execute_tap(self.get_create_activity_btn_ele())
