from BaseFramework.UIHelper.helper import Selenium_Helper

usernamexpath="xpath=//input[@id='txtUserID']"
passwordxpath="xpath=//input[@id='txtPassword']"
submitbuttonxpath = "xpath=//input[@id='btnLogin'"

class Login_page(Selenium_Helper):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.send_values(usernamexpath,username)
        self.send_values(passwordxpath,password)
        self.click_element(submitbuttonxpath)


    