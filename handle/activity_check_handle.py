import page
import base


class ActivityCheckHandle(page.ActivityCheckPage):

    def tap_activity_check(self):
        self.execute_tap(self.get_activity_check_ele())

    def switch_activity_check_frame(self):
        self.driver.switch_to.frame(self.get_activity_check_frame())

    def tap_activity_status(self):
        self.execute_tap(self.get_activity_status_ele())

    def tap_activity_status_confirm(self):
        self.execute_tap(self.get_activity_status_confirm_ele())

    def tap_activity_status_select(self):
        self.execute_tap(self.get_activity_status_select_ele())

    def tap_activity_check_btn(self):
        self.execute_tap(self.get_activity_check_btn_ele())