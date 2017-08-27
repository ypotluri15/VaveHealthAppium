'''
Created on Aug 27, 2017

@author: ypotluri
'''
"""
 VHealthTab Page
****************************
This  class provides the VHealthTab page object 
"""

import sys
import time

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import By
from robot.api import logger


sys.path.append('/Users/ypotluri/Documents/ws_shoretel/vave_health/src');





class VHealthTab():
    logger.info("LoginPage Called");
    
    def __init__(self, driver=None):
        self.driver = driver;
        
    def get_driver(self):
        return self.driver;
            
    def go_to_home(self):
        try:
            self.homeTab = self.get_driver().find_element_by_xpath("//XCUIElementTypeButton[@label='home outline Home']")
            time.sleep(1);
            self.homeTab.click();
        except:
            Exception
            logger.error("go to home navigation Failed");    
    
    def go_to_contact(self):
        try:
            self.contactTab = self.get_driver().find_element_by_xpath("//XCUIElementTypeButton[@label='contacts outline Contact']")
            time.sleep(1);
            self.contactTab.click();
        except:
                Exception
                logger.error("go to contact navigation Failed");    

    def go_to_about(self):
        try:
            self.aboutTab = self.get_driver().find_element_by_xpath("//XCUIElementTypeButton[@label='information circle-outline About']");
            self.aboutTab.click();
            time.sleep(3);
        except:
            Exception
            logger.error("go to about navigation Failed");    
        
    def navigate_tabs(self):

            logger.info("navigate_tabs Called");
            time.sleep(5);
            self.go_to_about();
            self.go_to_contact();
            self.go_to_home();
         
        