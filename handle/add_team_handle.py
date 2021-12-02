import page


class AddTeamHandle(page.AddTeamPage):

    def input_team_name(self, text):
        self.execute_input(self.get_team_name_ele(), text)

    def input_team_total_name(self, text):
        self.execute_input(self.get_team_total_name_ele(), text)

    def input_team_image(self, image_url):
        self.execute_input(self.get_team_image_ele(), image_url)

    def input_team_creater(self, team_creater):
        self.execute_input(self.get_team_creater_ele(), team_creater)

    def tap_team_yunying(self):
        self.execute_tap(self.get_team_yunying_ele())

    def input_team_yunying(self, team_yunying):
        self.execute_input(self.get_team_yunying_input_ele(), team_yunying)

    def tap_team_yunying_select(self):
        self.execute_tap(self.get_team_yunying_select_ele())

    def tap_team_yunying_choose(self):
        self.execute_tap(self.get_team_yunying_choose_ele())

    def tap_team_date(self):
        self.execute_tap(self.get_team_date_ele())

    def tap_team_date_confirm(self):
        self.execute_tap(self.get_team_date_confirm_ele())

    def tap_team_province(self):
        self.execute_tap(self.get_team_province_ele())

    def tap_team_province_confirm(self):
        self.execute_tap(self.get_team_province_confirm_ele())

    def tap_team_shi(self):
        self.execute_tap(self.get_team_shi_ele())

    def tap_team_shi_confirm(self):
        self.execute_tap(self.get_team_shi_confirm_ele())

    def tap_team_qu(self):
        self.execute_tap(self.get_team_qu_ele())

    def tap_team_qu_confirm(self):
        self.execute_tap(self.get_team_qu_confirm_ele())

    def input_team_office_address(self, team_office_address):
        self.execute_input(self.get_team_office_address_ele(), team_office_address)

    def input_team_connecter(self, team_connecter):
        self.execute_input(self.get_team_connecter_ele(), team_connecter)

    def input_team_phone(self, team_phone):
        self.execute_input(self.get_team_phone_ele(), team_phone)

    def tap_team_service(self):
        self.execute_tap(self.get_team_service_ele())

    def input_team_introduce(self, team_introduce):
        self.execute_input(self.get_team_introduce_ele(), team_introduce)

    def tap_team_create_btn(self):
        self.execute_tap(self.get_team_create_btn_ele())















