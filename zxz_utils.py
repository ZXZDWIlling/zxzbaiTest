from appium import webdriver
import unittest

# 设备Coolpad8720L-0x0da35366
Coolpad = dict(deviceName = 'Coolpad8720L-0x0da35366', platformVersion = '4.3')
Oppo = dict(deviceName = '93ee2ab6', platformVersion = '5.1.1')
Simulator_Nox = dict(deviceName = '127.0.0.1:62001', platformVersion = '4.4.2')
Huawei_H60 = dict(deviceName = 'X8QDU15C23028296', platformVersion = '4.4.2')

# device = Coolpad
# device = Oppo
device = Simulator_Nox
# device = Huawei_H60

class UiHelper:
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = device['platformVersion']
        self.desired_caps['deviceName'] = device['deviceName']
        self.desired_caps['appPackage'] = 'com.baibai.baibai'
        self.desired_caps['appActivity'] = '.view.activity.common.SplashActivity'
        self.desired_caps['automationName'] = "Uiautomator2"
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        pass

    def getWebDriver(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        return self.driver

    def quit(self):
        self.driver.quit()
        pass
