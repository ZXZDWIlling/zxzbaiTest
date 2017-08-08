from time import sleep
from appium import webdriver
from time import time
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

    def tearDown(self):
        self.driver.quit()
        pass

    # 获取启动页 + 广告页 时间
    def test_001_SplashTime(self):
        self.driver.wait_activity('.view.activity.common.SplashActivity', 60)
        start = time()
        self.driver.wait_activity('.view.activity.common.LoginActivity', 60)
        duration = time() - start
        print('启动页和广告页时间为{0}'.format(duration))
        pass

    # 执行登录参数列表
    def test_002_LoginCase(self):
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

            # 点击‘登录’按钮
            loginButton.click()
        pass

    def test_003_(self):
        self.driver.background_app(10)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
