from selenium.webdriver.common.by import By
import time
from BaseFramework.PreprocessingLogs.processinglogs import customLogger
import logging
log = customLogger(logging.DEBUG)
from datetime import datetime
now = datetime.now()
file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"

class Selenium_Helper:
    driver =''
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def launch_browser_url(self, browsername='Chrome', url='' ):
        driver_web = self.launch_browser(browsername)
        driver_web.get(url)
        return driver_web
    
    def _capture_screenshot(self,name=''):
     self.get_screenshot_as_file(name)

    def weblocator(self,locator=''):
        if locator.lower() == "id":
            log.info("webelement " + locator.upper() +
                        " Success..!")
            return By.ID
        elif locator.lower() == "xpath":
            log.info("webelement " + locator.upper() +
                        " Success..!")
            return By.XPATH
        
    def weblement(self, webelemntvalue=''):
        try:
            elemnt = webelemntvalue.split('=',1)
            locator = elemnt[0]
            weloc = elemnt[1]
            byclass = self.weblocator(locator)
            elem =  self.driver.find_element(byclass, weloc)
            log.info("webelement " + webelemntvalue.upper() +
                            " Success..!")
        except:
            self._capture_screenshot(file_name)
            log.info("webelement " + webelemntvalue.upper() +
                            " Failed..!")

        return elem
    
    def send_values(self,webelemntvalue='',values=''):
        try:
            ele = self.weblement(webelemntvalue)
            ele.clear()
            ele.send_keys(values)
            log.info("value passed to input " + values.upper() +
                            " Success..!")
            time.sleep(1)
        except:
            self._capture_screenshot(file_name)
            log.info("webelement " + webelemntvalue.upper() +
                            " Failed..!")
    
    def click_element(self,webelemntvalue=''):
        try:
            ele = self.weblement(webelemntvalue)
            log.info("Click Operation was Success..!")
            ele.click() 
        except:
            self._capture_screenshot(file_name)
            log.info("webelement " + webelemntvalue.upper() +
                            " Failed..!")