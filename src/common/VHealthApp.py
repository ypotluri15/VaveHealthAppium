'''
Created on Aug 26, 2017

@author: ypotluri
'''



import os
import sys

from appium import webdriver
from robot.api import logger


sys.path.append('/Users/ypotluri/Documents/ws_shoretel/vave_health/src');

class VHealthApp():

    def openApplication(self,udid):

                app = os.getenv('WORKSPACE_APP_FILE_LOC');
                if app is   None:
                    app = '/Users/ypotluri/Library/Developer/Xcode/DerivedData/MyApp-hbvtfxdxafumnlfaxvylnblelgsw/Build/Products/Debug-iphoneos/MyApp.app'
                self.driver = webdriver.Remote(
                        'http://127.0.0.1:4723/wd/hub',
                        {
                            'app': app,
                            'automationName':'XCUITest',
                            'deviceName': 'iPhone',
                            'device':'iOS',
                            'xcodeConfigFile':'/Users/ypotluri/xcconfig.cfg',
                            'platformName':'iOS',
                            'realDeviceLogger':'/usr/local/lib/node_modules/deviceconsole/deviceconsole',
                            'showIOSLog': 'true',
                            'showXcodeLog': 'true',
                            'udid':udid,
                            'realDeviceLogger': 'idevicesyslog',
                            'launchTimeout': '9000',
                            'clearSystemFiles':'True',
                            'bundleid':'io.ionic.starter',
                            'platformVersion':'10.3'   
                                 
                  
                        })
                return self.driver;

    def closeApplication(self):
            logger.info("shutdown driver called");

            self.driver.quit()


    def get_driver(self):
            logger.info("get driver called");
            return self.driver

