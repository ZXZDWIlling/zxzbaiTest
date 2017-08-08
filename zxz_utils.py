from appium import webdriver
import unittest

# 设备Coolpad8720L-0x0da35366
Coolpad = dict(deviceName = 'Coolpad8720L-0x0da35366', platformVersion = '4.3')
Oppo = dict(deviceName = '93ee2ab6', platformVersion = '5.1.1')
Simulator_Nox = dict(deviceName = '127.0.0.1:62001', platformVersion = '4.4.2')

# device = Coolpad
# device = Oppo
device = Simulator_Nox


class UiHelper:
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = device['platformVersion']
        self.desired_caps['deviceName'] = device['deviceName']
        self.desired_caps['appPackage'] = 'com.baibai.baibai'
        self.desired_caps['appActivity'] = '.view.activity.common.SplashActivity'
        pass

    def getWebDriver(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        return self.driver

    def quit(self):
        self.driver.quit()
        pass
