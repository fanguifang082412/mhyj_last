from selenium.webdriver.common.by import By

import base


class AddTeamPage(base.ActionElement):
    team_name_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[1]/div/div[1]/input'
    team_total_name_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[2]/div/div[1]/input'
    team_image_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[3]/div/div/div/input'
    team_creater_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[4]/div/div/input'
    team_yunying_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[5]/div/div/div/button'
    team_yunying_input_feature = By.XPATH, '/html/body/div[2]/div/div[2]/form/div[1]/div/div/input'
    team_yunying_select_feature = By.XPATH, '/html/body/div[2]/div/div[2]/form/div[2]/div/button/span'
    team_yunying_choose_feature = By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/button/span'
    team_date_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[6]/div/div/input'
    team_date_confirm_feature = By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[5]/div/span'
    team_province_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[7]/div/div[1]/div/div/div/div[1]/input'
    team_province_confirm_feature = By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span'
    team_shi_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[7]/div/div[2]/div/div/div/div[1]/input'
    team_shi_confirm_feature = By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li/span'
    team_qu_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[7]/div/div[3]/div/div/div/div/input'
    team_qu_confirm_feature = By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[2]/span'
    team_office_address_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[8]/div/div[1]/input'
    team_connecter_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[9]/div/div[1]/input'
    team_phone_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[10]/div/div[1]/input'
    team_service_range = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[11]/div/div/label[1]/span[2]'
    team_introduce_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[12]/div/div[1]/textarea'
    team_create_btn_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[13]/div/button[1]/span'


    def get_team_name_ele(self):
        return self.get_element(self.team_name_feature)

    def get_team_total_name_ele(self):
        return self.get_element(self.team_total_name_feature)

    def get_team_image_ele(self):
        return self.get_element(self.team_image_feature)

    def get_team_creater_ele(self):
        return self.get_element(self.team_creater_feature)

    def get_team_yunying_ele(self):
        return self.get_element(self.team_yunying_feature)

    def get_team_yunying_input_ele(self):
        return self.get_element(self.team_yunying_input_feature)

    def get_team_yunying_select_ele(self):
        return self.get_element(self.team_yunying_select_feature)

    def get_team_yunying_choose_ele(self):
        return self.get_element(self.team_yunying_choose_feature)

    def get_team_date_ele(self):
        return self.get_element(self.team_date_feature)

    def get_team_date_confirm_ele(self):
        return self.get_element(self.team_date_confirm_feature)

    def get_team_province_ele(self):
        return self.get_element(self.team_province_feature)

    def get_team_province_confirm_ele(self):
        return self.get_element(self.team_province_confirm_feature)

    def get_team_shi_ele(self):
        return self.get_element(self.team_shi_feature)

    def get_team_shi_confirm_ele(self):
        return self.get_element(self.team_shi_confirm_feature)

    def get_team_qu_ele(self):
        return self.get_element(self.team_qu_feature)

    def get_team_qu_confirm_ele(self):
        return self.get_element(self.team_qu_confirm_feature)

    def get_team_office_address_ele(self):
        return self.get_element(self.team_office_address_feature)

    def get_team_connecter_ele(self):
        return self.get_element(self.team_connecter_feature)

    def get_team_phone_ele(self):
        return self.get_element(self.team_phone_feature)

    def get_team_service_ele(self):
        return self.get_element(self.team_service_range)

    def get_team_introduce_ele(self):
        return self.get_element(self.team_introduce_feature)

    def get_team_create_btn_ele(self):
        return self.get_element(self.team_create_btn_feature)


