from selenium import webdriver
from selenium.webdriver import chrome, ChromeOptions, ChromeService
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import os
import sys
sys.path.insert(1, os.getcwd())
from BaseFramework.PreprocessingLogs.processinglogs import customLogger
import logging


class WebDriver:
    driver_ele=''
    def __init__(self) -> None:
        pass
    log = customLogger(logLevel=logging.DEBUG)
    def launch_browser(self, browser=''):
        global driver_ele
        if browser.lower() == 'chrome':
            options =  ChromeOptions()
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            # driver.get("https://www.google.com")
            time.sleep(5)
            driver_ele = driver
            self.log.info("Launch Driver type " + browser.upper() +
                        " Success..!")
            return driver_ele
        elif browser.lower() == 'firefox':
            pass
    def launch_browser_url(self, browsername='Chrome', url='' ):
        driver_web = self.launch_browser(browsername)
        driver_web.get(url)
        return driver_web

    def weblocator(self,locator=''):
        if locator.lower() == "id":
            return By.ID
        elif locator.lower() == "xpath":
            return By.XPATH
        
    def weblement(self, webelemntvalue=''):
        elemnt = webelemntvalue.split('=',1)
        locator = elemnt[0]
        weloc = elemnt[1]
        byclass = self.weblocator(locator)
        elem =  driver_ele.find_element(byclass, weloc)
        self.log.info("webelement " + webelemntvalue.upper() +
                        " Success..!")
        return elem
    
    def send_values(self,webelemntvalue='',values=''):
        ele = self.weblement(webelemntvalue)
        ele.clear()
        ele.send_keys(values)
        self.log.info("value passed to input " + values.upper() +
                        " Success..!")
        time.sleep(1)
    
    def click_element(self,webelemntvalue=''):
        ele = self.weblement(webelemntvalue)
        self.log.info("Click Operation was Success..!")
        ele.click()


# clss = WebDriver()
# clss.launch_browser("chrome")
# # clss.weblement("xpath=//textarea[@name='q']").send_keys("vinay")
# clss.send_values("xpath=//textarea[@name='q']","Vinay kumar")