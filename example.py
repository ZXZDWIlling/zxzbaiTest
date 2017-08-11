from appium import webdriver
import unittest

class TestStudy(unittest.TestCase):
    #初始化
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.baibai.baibai'
        desired_caps['appActivity'] = '.view.activity.common.SplashActivity'
        #启动
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps);
        pass

    def atearDown(self):
        self.driver.quit()
        pass

    def testDemo1(self):
        a = self.driver.get_window_size()['height']
        b = self.driver.get_window_size()['width']
        sleep(1)
        self.driver.swipe(100, 100, 100, 400, 8000)
        print(a)
        print(b)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStudy)
    unittest.TextTestRunner(verbosity=2).run(suite)
