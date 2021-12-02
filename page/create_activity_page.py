from selenium.webdriver.common.by import By
import base


class CreateActivityPage(base.ActionElement):
    create_activity_frame = By.XPATH, '//*[@id="content-main"]/iframe[3]'
    volunteer_team_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[2]/div/div/input'
    volunteer_team_input_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/input'
    volunteer_team_select_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/button/i'
    activity_volunteer_team_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/table/tbody/tr[1]/td[2]/div'
    activity_volunteer_team_confirm_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/div/button[2]'
    activity_participants_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[3]/div[3]/div[1]/div/div/div/input'
    activity_name_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[5]/div/div/input'
    activity_start_time_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[9]/div/div[1]/div/div/div[1]/input'
    activity_start_time_confirm_feature = By.XPATH, '/html/body/div[3]/div[1]/div/div[3]/table[1]/tbody/tr[7]/td[7]/div/span'
    activity_end_time_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[9]/div/div[2]/div/div/div/input'
    activity_end_time_confirm_feature = By.XPATH, '/html/body/div[4]/div[2]/button[2]'
    activity_address_input_feature = By.XPATH, '//*[@id="tipinput"]'
    activity_address_confirm_feature = By.XPATH, '//*[@id="amap-sug0"]/span'
    activity_detail_address_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[10]/div/div[2]/div/div/div/input'
    activity_coordinates_address_feature = By.XPATH, '//*[@id="container"]/div[1]/div/div[1]/div[1]'
    create_activity_btn_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/footer/button'

    def get_create_activity_frame(self):
        return self.get_element(self.create_activity_frame)

    def get_volunteer_team_ele(self):
        return self.get_element(self.volunteer_team_feature)

    def get_volunteer_team_input_ele(self):
        return self.get_element(self.volunteer_team_input_feature)

    def get_volunteer_team_select_ele(self):
        return self.get_element(self.volunteer_team_select_feature)

    def get_activity_volunteer_team_ele(self):
        return self.get_element(self.activity_volunteer_team_feature)

    def get_activity_volunteer_team_confirm_ele(self):
        return self.get_element(self.activity_volunteer_team_confirm_feature)

    def get_activity_participants_ele(self):
        return self.get_element(self.activity_participants_feature)

    def get_activity_name_ele(self):
        return self.get_element(self.activity_name_feature)

    def get_activity_start_time_ele(self):
        return self.get_element(self.activity_start_time_feature)

    def get_activity_start_time_confirm_ele(self):
        return self.get_element(self.activity_start_time_confirm_feature)

    def get_activity_end_time_ele(self):
        return self.get_element(self.activity_end_time_feature)

    def get_activity_end_time_confirm_ele(self):
        return self.get_element(self.activity_end_time_confirm_feature)

    def get_activity_address_input_ele(self):
        return self.get_element(self.activity_address_input_feature)

    def get_activity_address_confirm_ele(self):
        return self.get_element(self.activity_address_confirm_feature)

    def get_activity_detail_address_ele(self):
        return self.get_element(self.activity_detail_address_feature)

    def get_activity_coordinates_address_ele(self):
        return self.get_element(self.activity_coordinates_address_feature)

    def get_create_activity_btn_ele(self):
        return self.get_element(self.create_activity_btn_feature)



