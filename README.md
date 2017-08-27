# VaveHealthAppium

Prerequisites:

1. Eclipse
2. xCode
3. ionic
4. python
5. Appium
6. Webdriver Agent

Installation steps:

if the above dependencies are not installed, follow the steps from 1 to 7, otherwise skip to project setup

1.Install node
         brew install node
 
2.Appium (current version 1.6.3)
          npm install -g appium
 
3. Appium python client libraries
          pip install Appium-Python-Client
 
4. Install Carthage 
	https://github.com/Carthage/Carthage/releases
	Run ./Scripts/bootstrap.h from /usr/local/lib/node_modules/appium/WebdriverAgent
 
5.libimobile device
             brew install libimobiledevice

6. Webdriver agent (Clone the project and build it via Xcode)
	 https://github.com/facebook/WebDriverAgent
	Copy Webdriver agent to /usr/local/lib/node_modules

 
7. Eclipse for IOS with Pydev  
             Pydev  - Python plug in 


Project setup


1.Clone the project from GIT

2.Import project in Eclipse as Python Project
   Eclipse > File > Import >
   Select the src code downloaded in step 1
   
3.Change Below Configurations
     a.class login_test(unittest.TestCase):
        self.driver = self.vHealthApp.openApplication('0ae97168045f951421e9def5b9dff64c68383607');
         Replace 0ae97168045f951421e9def5b9dff64c68383607 UDID with your device UDID
         
     b.Replace below line App Path in file VHealthApp.py (Copied from ionic project derived data path)
     app = '/Users/ypotluri/Library/Developer/Xcode/DerivedData/MyApp-hbvtfxdxafumnlfaxvylnblelgsw/Build/Products/Debug-iphoneos/MyApp.app'

4.Open Terminal 

5.Launch Appium Server by giving your device UDID 
	appium -a localhost -U udid
	appium -a localhost -U  0ae97168045f951421e9def5b9dff64c68383607

6.Go to Eclipse > select file > test/login_test >  Run as python unit test
    
