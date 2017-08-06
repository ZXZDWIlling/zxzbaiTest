from time import sleep
from appium import webdriver
import unittest
import sys

class LoginTest(unittest.TestCase):
    # 初始化
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '93ee2ab6'
        desired_caps['appPackage'] = 'com.baibai.baibai'
        desired_caps['appActivity'] = '.view.activity.common.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        pass
    def tearDown(self):
        self.driver.quit()
        pass
    # def testSplashTime(self):
    #     pass
    def testLogin(self):
        self.driver.wait_activity('.view.activity.common.LoginActivity', 60)
        phoneEdit = self.driver.find_element_by_id('com.baibai.baibai:id/et_account')
        print(self.driver.current_activity)
        phoneEdit.click()
        phoneEdit.send_keys('1222')
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
