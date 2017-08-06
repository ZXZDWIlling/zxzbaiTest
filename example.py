from appium import webdriver
import unittest

class TestStudy(unittest.TestCase):
    #初始化
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '93ee2ab6'
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        #启动
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps);
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    def testDemo1(self):
        urlEdit = self.driver.find_element_by_id('com.android.contacts:id/create_contact_button')
        urlEdit.click()
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStudy)
    unittest.TextTestRunner(verbosity=2).run(suite)
