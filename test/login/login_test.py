'''
Created on Aug 26, 2017

@author: ypotluri
'''

import os
import sys
import unittest
from pages.LoginPage import LoginPage
from pages.VHealthTabs import VHealthTab
from common.VHealthApp import VHealthApp;

sys.path.append(os.getcwd() + "/src")
sys.path.append(os.getcwd() + "/test")


class login_test(unittest.TestCase):
    def setUp(self):
        self.vHealthApp = VHealthApp();
        self.driver = self.vHealthApp.openApplication('0ae97168045f951421e9def5b9dff64c68383607');
        
    def tearDown(self):
        self.driver.quit();
        
    def test_basicNavigation(self):
        vhealthtab = VHealthTab(self.driver);
        vhealthtab.navigate_tabs();        
        loginPage = LoginPage(self.driver);
        loginPage.set_login_username("yogitapotluri");
        loginPage.set_password("vavehealth");
        loginPage.set_description("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vel justo ullamcorper, rutrum libero quis, iaculis mauris. Aenean et risus est. Sed maximus risus in odio luctus, a aliquam nisl pulvinar. Aliquam nec ligula ut tellus volutpat commodo vitae id elit. Morbi viverra scelerisque rutrum. Phasellus tempor eget purus ut maximus. Nulla facilisis, mauris ac ornare consectetur, enim turpis ullamcorper lectus, in molestie metus nulla quis libero. Vestibulum lacus mauris, pretium eu vestibulum eget, tincidunt quis mauris. Phasellus metus libero, accumsan ut vehicula non, euismod sit amet ante");
        loginPage.click_submit();
        
        vhealthtab = VHealthTab(self.driver);
        vhealthtab.navigate_tabs();
        
        
if __name__ == '__main__':
    home_page_test = unittest.TestLoader().loadTestsFromTestCase(login_test)
    test_suite = unittest.TestSuite([home_page_test])
    unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    