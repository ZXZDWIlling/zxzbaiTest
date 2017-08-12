from time import sleep
from appium import webdriver
from time import time
import os
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from baibai.baibai_operation import BaiBai_App
from zxz.zxz_utils import UiHelper

login_cases = []
login_cases.append(dict(phone = '', password = '', desc = '全部不输入，登录失败'))
login_cases.append(dict(phone = '', password = '123456', desc = '不输入手机号，登录失败'))
login_cases.append(dict(phone = '18819425652', password = '123456', desc = '没有注册过的手机号，登录失败'))
login_cases.append(dict(phone = '05521397022', password = '', desc = '不输入密码，登录失败'))
login_cases.append(dict(phone = '05521397022', password = '1234567', desc = '密码错误，登录失败'))
login_cases.append(dict(phone = '05521397022', password = '123456', desc = '手机号、密码正确，登录成功'))

class LoginTest(unittest.TestCase):
    '''测试开始前，务必确认已经退出登陆。。。'''

    # 初始化
    def setUp(self):
        self.helper = UiHelper()
        self.driver = self.helper.getWebDriver()
        pass

    # 测试结束
    def tearDown(self):
        self.driver.quit()
        pass

    # 获取启动页 + 广告页 时间
    def test_001_SplashTime(self):
        '''测试启动页和广告页的启动时间。。。'''

        self.driver.wait_activity('.view.activity.common.SplashActivity', 60)
        start = time()
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located(\
            (By.ID, 'com.baibai.baibai:id/splash_iv')))
        duration = time() - start
        print('启动页和广告页时间为{0}'.format(duration))
        pass

    # 执行登录参数列表
    def test_002_LoginCase(self):
        '''执行参数列表。。。

        '''
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

    def test_003_AutoLogin(self):
        '''验证自动登陆的功能。。。'''

        self.driver.wait_activity('.view.activity.MainActivity', 60)
        self.assertEqual('.view.activity.MainActivity', self.driver.current_activity)
        
        print('杀死进程，再进入，能自动登录', '*' * 20)
        os.system('adb shell am force-stop com.baibai.baibai')
        self.driver.start_activity('com.baibai.baibai', '.view.activity.common.SplashActivity')
        self.driver.wait_activity('.view.activity.MainActivity', 30)
        self.assertEqual('.view.activity.MainActivity', self.driver.current_activity)

        print('退出登陆', '*' * 20)
        userCenterEntry = self.driver.find_element_by_id('com.baibai.baibai:id/rb_4')
        userCenterEntry.click()
        # 找到退出按钮
        exitButton = self.helper.scrollToElementByName('退出')
        self.assertIsNotNone(exitButton)

        # 验证点击'取消',取消退出登陆
        print('1)验证点击"取消",取消退出登陆')
        exitButton.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(\
            (By.ID, 'com.baibai.baibai:id/tipTv')))
        sureButton = self.driver.find_element_by_id('com.baibai.baibai:id/sureTv')
        cancelButton = self.driver.find_element_by_id('com.baibai.baibai:id/cancleTv')
        cancelButton.click()
        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located(\
            (By.ID, 'com.baibai.baibai:id/tipTv')))

        # 验证按返回键,取消退出登陆
        print('2)验证按返回键,取消退出登陆')
        exitButton.click()
        self.driver.press_keycode('4')
        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located(\
            (By.ID, 'com.baibai.baibai:id/tipTv')))

        # 验证退出登陆
        print('3)验证退出登陆')
        exitButton.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(\
            (By.ID, 'com.baibai.baibai:id/tipTv')))
        sureButton.click()
        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located(\
            (By.ID, 'com.baibai.baibai:id/tipTv')))
        # BaiBai_App(self.driver, self.helper).exit_app()
        # 强制杀死进程，重新登陆
        os.system('adb shell am force-stop com.baibai.baibai')
        self.driver.start_activity('com.baibai.baibai', '.view.activity.common.SplashActivity')
        self.driver.wait_activity('.view.activity.common.LoginActivity', 60)
        self.assertEqual(self.driver.current_activity, '.view.activity.common.LoginActivity')
        pass



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
