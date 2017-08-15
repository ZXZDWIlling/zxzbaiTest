from appium import webdriver

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
        # 设备参数
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = device['platformVersion']
        self.desired_caps['deviceName'] = device['deviceName']
        self.desired_caps['appPackage'] = 'com.baibai.baibai'
        self.desired_caps['appActivity'] = '.view.activity.common.SplashActivity'
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        # 初始化工具
        self.driver = None
        self.window_size = {}
        pass

    def getWebDriver(self):
        '''获取appium的WebDriver'''
        if None == self.driver:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        return self.driver

    def quit(self):
        self.driver.quit()
        pass

    # 获取屏幕大小
    def getWindowSize(self):
        '''获取屏幕大小
        返回屏幕大小的字典，字段为width和height'''
        if 0 == len(self.window_size):
            self.window_size['width'] = self.getWebDriver().get_window_size()['width']
            self.window_size['height'] = self.getWebDriver().get_window_size()['height']
        return self.window_size
        pass

    # 根据屏幕比例，执行滑动操作
    def swipeByPercentage(self, start_x_percent, start_y_percent, end_x_percent, end_y_percent, time = 2000):
        '''根据屏幕比例，执行滑动操作
        返回bool值，滑动成功返回True，否则返回False'''
        # 获取屏幕大小
        width = self.getWindowSize()['width']
        height = self.getWindowSize()['height']
        # 滑动
        pre = self.getWebDriver().page_source
        self.getWebDriver().swipe(width * start_x_percent, height * start_y_percent\
            , width * end_x_percent, height * end_y_percent, time)
        cur = self.getWebDriver().page_source
        # 判断滑动是否成功
        return pre != cur
        pass

    # 滑动到最底部
    def swipeToBottom(self, time = 2000, start_x_percent = 1/2, start_y_percent = 3/4, end_x_percent = 1/2, end_y_percent = 1/4):
        '''滑动到最底部'''
        while True:
            ret = self.swipeByPercentage(start_x_percent, start_y_percent, end_x_percent, end_y_percent, time)
            # print('滑动')
            if not ret:break
        pass

    # 向下滑动
    def swipeDown(self, time = 2000, start_x_percent = 1/2, start_y_percent = 1/4, end_x_percent = 1/2, end_y_percent = 3/4):
        '''向下滑动
        返回bool值，滑动成功返回True，否则返回False'''
        # 滑动
        return self.swipeByPercentage(start_x_percent, start_y_percent, end_x_percent, end_y_percent, time)
        pass

    # 向上滑动
    def swipeUp(self, time = 2000, start_x_percent = 1/4, start_y_percent = 3/4, end_x_percent = 1/4, end_y_percent = 1/4):
        '''向上滑动
        返回bool值，滑动成功返回True，否则返回False'''
        # 滑动
        return self.swipeByPercentage(start_x_percent, start_y_percent, end_x_percent, end_y_percent, time)
        pass

    # 滑动到某个组件
    def scrollToElementById(self, id, attemp = 10, time = 2000):
        '''滑动到某个组件'''
        while attemp > 0:
            try:
                element = self.getWebDriver().find_element_by_id(id)
                return element
            except:
                attemp -= 1
                self.swipeUp()
            # element.location_once_scrolled_into_view()
        return None
        pass

    # 滑动到某个组件
    def scrollToElementByName(self, name, attemp = 10, time = 2000):
        '''滑动到某个组件'''
        while attemp > 0:
            try:
                element = self.getWebDriver().find_element_by_name(name)
                return element
            except:
                attemp -= 1
                self.swipeUp()
        return None
        pass

    def getScrollListItems(self, parent, son):
        pass
