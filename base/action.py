import json
from selenium.webdriver.support.wait import WebDriverWait



class ActionElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, feature):
        try:
            ele = WebDriverWait(self.driver, 15, 0.5).until(lambda x: x.find_element(*feature))

        except Exception as e:
            return None

        else:
            return ele

    def execute_input(self, feature, text):
        if isinstance(feature, tuple):
            self.get_element(feature).send_keys(text)

        else:
            feature.send_keys(text)

    def execute_tap(self, feature):
        if isinstance(feature, tuple):
            self.get_element(feature).click()

        else:
            feature.click()

    @classmethod
    def get_data(cls, filename, data_demo):
        list = []
        with open("./data/%s.json" % filename, encoding="utf-8") as f:
            data = json.load(f).get(data_demo)
            for i in data.values():
                list.append(i)
        return list




