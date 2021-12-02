import allure
import base
import page


driver = base.DriverUntil.get_driver()


class PageHandle(page.PageLogin):


    @allure.step("输入用户名")
    def input_username(self, username):
        allure.attach("输入用户名为：", "%s" % username)
        self.execute_input(self.get_username_ele(), username)

    @allure.step("输入密码")
    def input_pwd(self, pwd):
        allure.attach("输入密码为：", "密码为%s" % pwd)
        self.execute_input(self.get_pwd_ele(), pwd)

    @allure.step("点击登录按钮")
    def tap_login_btn(self):
        # allure.attach("这是登录后的截图", driver.get_screen_shot_as_png(), allure.attachment_type.PNG)
        self.execute_tap(self.get_login_ele())

    def go_login(self, username, pwd):
        self.input_username(username)
        self.input_pwd(pwd)
        self.tap_login_btn()