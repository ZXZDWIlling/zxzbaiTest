from time import sleep
from appium import webdriver
import unittest

login_cases = []
login_cases.append(dict(phone = '', password = None, desc = '全部不输入，登录失败'))
login_cases.append(dict(phone = '', password = '123456', desc = '不输入手机号，登录失败'))
login_cases.append(dict(phone = '18819425652', password = '123456', desc = '没有注册过的手机号，登录失败'))
login_cases.append(dict(phone = '15521397022', password = '', desc = '不输入密码，登录失败'))
login_cases.append(dict(phone = '15521397022', password = '1234567', desc = '密码错误，登录失败'))
login_cases.append(dict(phone = '15521397022', password = '123456', desc = '手机号、密码正确，登录失败'))

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

    def testLogin(self):
        self.driver.wait_activity('.view.activity.common.LoginActivity', 60)
        phoneEdit = self.driver.find_element_by_id('com.baibai.baibai:id/et_account')
        passwordEdit = self.driver.find_element_by_id('com.baibai.baibai:id/et_password')
        print(self.driver.current_activity)
        # phoneEdit.click()
        for i in range(len(login_cases)):
            if '' == login_cases[i]['phone']:
                phoneEdit.clear()
            else:
                phoneEdit.send_keys(login_cases[i]['phone'])
            self.assertEqual(send_keys(login_cases[i]['phone'], phoneEdit.text \
            , '预期: {0}, 实际: {1}'.format(login_cases[i]['phone'], phoneEdit.text()))
            if None == login_cases[i]['password']:
                passwordEdit.clear()
            else:
                passwordEdit.send_keys(login_cases[i]['password'])
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
