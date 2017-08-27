'''
Created on Aug 26, 2017

@author: ypotluri
'''
"""
 Login Page
****************************
This  class provides the login page object 
"""

import sys

from appium.webdriver.webdriver import WebDriver
from robot.api import logger


sys.path.append('/Users/ypotluri/Documents/ws_shoretel/vave_health/src');


class LoginPage():
    logger.info("LoginPage Called");
    
    def __init__(self, driver=None):
        self.driver = driver;
        
    def get_driver(self):
        return self.driver;
            
    def set_login_username(self,username):

        logger.info("set_login_username Called");
        self.usernameInput = self.get_driver().find_element_by_xpath("//XCUIElementTypeStaticText[@label='Username']")
        self.usernameInput.set_value(username);
        
    def set_password(self, password):
        logger.info("set_password Called");
        self.passwordInput = self.get_driver().find_element_by_xpath("//XCUIElementTypeStaticText[@label='Password']");
        self.passwordInput.set_value(password);
    def set_description(self, description):
        logger.info("set_password Called");
        self.descriptionInput = self.get_driver().find_element_by_xpath("//XCUIElementTypeStaticText[@label='Description']");
        self.descriptionInput.set_value(description);
    
    def click_submit(self):
        logger.info("click_submit Called");
        self.submit = self.get_driver().find_element_by_xpath("//XCUIElementTypeButton[@label='Submit']");
        self.submit.click();
   
    