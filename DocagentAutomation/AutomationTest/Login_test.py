import pytest
import os
import sys
sys.path.insert(1, os.getcwd())
from conftest import *
# from DocagentAutomation.AutomationTest.conftest import Conftest
from DocagentAutomation.ObjectRepository.loginpage import Login_page

@pytest.mark.usefixtures("browser_setup")
class Test_login():

    def setup_class(self):
        self.driver.get(url)
        self.login_page = Login_page(self.driver)

    def test_valid_login(self):
        self.login_page.login(user_name, password_user)

    # def teardown_class(self):
    #     self.driver.quit()



# request.setup("chrome", "https://demo.docagent.net/R21V1UAT/default.aspx?","administrator","ddi@123" ) == True
 

