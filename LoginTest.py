from time import sleep
from appium import webdriver
from time import time
from uiautomator import device as d
import os
import unittest
import zxz_utils

login_cases = []
login_cases.append(dict(phone = '', password = '', desc = '全部不输入，登录失败'))
login_cases.append(dict(phone = '', password = '123456', desc = '不输入手机号，登录失败'))
login_cases.append(dict(phone = '18819425652', password = '123456', desc = '没有注册过的手机号，登录失败'))
login_cases.append(dict(phone = '10521397022', password = '', desc = '不输入密码，登录失败'))
login_cases.append(dict(phone = '10521397022', password = '1234567', desc = '密码错误，登录失败'))
login_cases.append(dict(phone = '10521397022', password = '123456', desc = '手机号、密码正确，登录成功'))

class LoginTest(unittest.TestCase):

    # 初始化
    def setUp(self):
        self.driver = zxz_utils.UiHelper().getWebDriver()
        pass

    # 测试结束
    def tearDown(self):
        self.driver.quit()
        pass

    # 获取启动页 + 广告页 时间
    def atest_001_SplashTime(self):
        self.driver.wait_activity('.view.activity.common.SplashActivity', 60)
        start = time()
        self.driver.wait_activity('.view.activity.common.LoginActivity', 60)
        duration = time() - start
        print('启动页和广告页时间为{0}'.format(duration))
        pass

    # 执行登录参数列表
    def atest_002_LoginCase(self):
        self.driver.wait_activity('.view.activity.common.LoginActivity', 60)
        phoneEdit = self.driver.find_element_by_id('com.baibai.baibai:id/et_account')
        passwordEdit = self.driver.find_element_by_id('com.baibai.baibai:id/et_password')
        loginButton = self.driver.find_element_by_id('com.baibai.baibai:id/tv_login')

        # 执行用例
        for i in range(len(login_cases)):
            print('正在执行用例，手机号：', login_cases[i]['phone'], '\t密码：', login_cases[i]['password'],\
                '预期结果：', login_cases[i]['desc'])
            # 输入手机号
            if '' == login_cases[i]['phone']:
                phoneEdit.clear()
                self.assertEqual('手机号', phoneEdit.text, \
                    '手机号, 预期: {0}, 实际: {1}'.format('手机号', phoneEdit.text))
            else:
                phoneEdit.send_keys(login_cases[i]['phone'])
                self.assertEqual(login_cases[i]['phone'], phoneEdit.text, \
                    '手机号, 预期: {0}, 实际: {1}'.format(login_cases[i]['phone'], phoneEdit.text))
            # 输入密码
            if '' == login_cases[i]['password']:
                passwordEdit.clear()
            else:
                passwordEdit.send_keys(login_cases[i]['password'])
                pass
            # 点击‘登录’按钮
            loginButton.click()
            pass
        pass

    def test_003_(self):
        print('验证默认自动登录')
        self.driver.wait_activity('.view.activity.MainActivity', 30)
        self.assertEqual('.view.activity.MainActivity', self.driver.current_activity)

        # print('杀死进程，再进入，能自动登录')
        # os.system('adb shell am force-stop com.baibai.baibai')
        # self.driver.start_activity('com.baibai.baibai', '.view.activity.common.SplashActivity')
        # self.driver.wait_activity('.view.activity.MainActivity', 30)
        # self.assertEqual('.view.activity.MainActivity', self.driver.current_activity)

        userCenterEntry = self.driver.find_element_by_id('com.baibai.baibai:id/rb_4')
        userCenterEntry.click()
        # userCerter = self.driver.find_element_by_id('com.baibai.baibai:id/rv_game_homepage')

        # self.driver.find_element_by_android_uiautomator()
        # a.click()
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
