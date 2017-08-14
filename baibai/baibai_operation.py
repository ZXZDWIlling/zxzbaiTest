from appium import webdriver
import unittest
from zxz.zxz_utils import UiHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaiBai_App:
    '''封装对Android拜拜产品的部分操作
    更新到1.0.19'''

    def __init__(self, driver = None, helper = None):
        self.driver = driver
        self.helper = helper
        pass

    def get_package(self):
        '''获取拜拜包名'''
        return 'com.baibai.baibai'

    def get_start_activity(self):
        '''获取启动activity名'''
        return '.view.activity.common.SplashActivity'

    def get_home_activity(self):
        '''获取首页activity'''
        return '.view.activity.MainActivity'

    def exit_app(self):
        '''退出app
        执行前请确认在app首页'''
        self.driver.wait_activity('.view.activity.MainActivity', 60)
        userCenterEntry = self.driver.find_element_by_id('com.baibai.baibai:id/rb_4')
        userCenterEntry.click()
        # 找到退出按钮
        exitButton = self.helper.scrollToElementByName('退出')
        exitButton.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(\
            (By.ID, 'com.baibai.baibai:id/sureTv')))
        self.driver.find_element_by_id('com.baibai.baibai:id/sureTv').click()
        pass

    def input_account_password(self, account, passwourd):
        '''登录'''
        self.driver.wait_activity('.view.activity.common.LoginActivity', 60)
        phoneEdit = self.driver.find_element_by_id('com.baibai.baibai:id/et_account')
        passwordEdit = self.driver.find_element_by_id('com.baibai.baibai:id/et_password')
        loginButton = self.driver.find_element_by_id('com.baibai.baibai:id/tv_login')
        phoneEdit.send_keys(account)
        passwordEdit.send_keys(passwourd)
        loginButton.click()
        self.driver.wait_activity('.view.activity.common.GuideActivity', 30)
        enterButton = self.driver.find_element_by_id('com.baibai.baibai:id/guide_start_tv')
        enterButton.click()
        pass
