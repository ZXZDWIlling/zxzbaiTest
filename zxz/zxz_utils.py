from appium import webdriver

# 设备Coolpad8720L-0x0da35366
Coolpad = dict(deviceName='Coolpad8720L-0x0da35366', platformVersion='4.3')
Oppo = dict(deviceName = '93ee2ab6', platformVersion='5.1.1')
Simulator_Nox = dict(deviceName='127.0.0.1:62001', platformVersion='4.4.2')
Huawei_H60 = dict(deviceName='X8QDU15C23028296', platformVersion='4.4.2')

# device = Coolpad
# device = Oppo
device = Simulator_Nox
# device = Huawei_H60


class UiHelper:

    def __init__(self):
        # 设备参数
        self.desired_caps = dict()
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = device['platformVersion']
        self.desired_caps['deviceName'] = device['deviceName']
        self.desired_caps['appPackage'] = 'com.baibai.baibai'
        self.desired_caps['appActivity'] = '.view.activity.common.SplashActivity'
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        # 初始化工具
        self.driver = None
        self.window_size = None
        pass

    def get_appium_driver(self):
        """获取Appium的WebDriver"""
        if self.driver is None:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        return self.driver

    def quit(self):
        self.driver.quit()
        pass

    # 获取屏幕大小
    def get_window_size(self):
        """获取屏幕大小
        返回屏幕大小的字典，字段为width和height"""
        if self.window_size is None:
            self.window_size = dict()
            self.window_size['width'] = self.get_appium_driver().get_window_size()['width']
            self.window_size['height'] = self.get_appium_driver().get_window_size()['height']
        return self.window_size
        pass

    # 根据屏幕比例，执行滑动操作
    def swipe_by_percentage(self, start_x_percent, start_y_percent, end_x_percent, end_y_percent, time=2000):
        """根据屏幕比例，执行滑动操作
        返回bool值，滑动成功返回True，否则返回False"""
        # 获取屏幕大小
        width = self.get_window_size()['width']
        height = self.get_window_size()['height']
        # 滑动
        pre = self.get_appium_driver().page_source
        self.get_appium_driver().swipe(width * start_x_percent, height * start_y_percent, width * end_x_percent, \
                                       height * end_y_percent, time)
        cur = self.get_appium_driver().page_source
        # 判断滑动是否成功
        return pre != cur
        pass

    # 滑动到最底部
    def swipe_to_bottom(self, time=2000, start_x_percent=1/2, start_y_percent=3/4, end_x_percent=1/2, end_y_percent=1/4):
        """滑动到最底部"""
        while True:
            ret = self.swipe_by_percentage(start_x_percent, start_y_percent, end_x_percent, end_y_percent, time)
            # print('滑动')
            if not ret:break
        pass

    # 向下滑动
    def swipe_down(self, time=2000, start_x_percent=1/2, start_y_percent=1/4, end_x_percent=1/2, end_y_percent=3/4):
        """向下滑动
        返回bool值，滑动成功返回True，否则返回False"""
        # 滑动
        return self.swipe_by_percentage(start_x_percent, start_y_percent, end_x_percent, end_y_percent, time)
        pass

    # 向上滑动
    def swipe_up(self, time=2000, start_x_percent=1/4, start_y_percent=3/4, end_x_percent=1/4, end_y_percent=1/4):
        """向上滑动
        返回bool值，滑动成功返回True，否则返回False"""
        # 滑动
        return self.swipe_by_percentage(start_x_percent, start_y_percent, end_x_percent, end_y_percent, time)
        pass

    # 滑动到某个组件
    def scroll_to_element_by_id(self, element_id, attempt=10, time=2000):
        """滑动到某个组件"""
        while attempt > 0:
            try:
                element = self.get_appium_driver().find_element_by_id(element_id)
                return element
            except:
                attempt -= 1
                self.swipe_up(time=time)
            # element.location_once_scrolled_into_view()
        return None
        pass

    # 滑动到某个组件
    def scroll_to_element_by_name(self, name, attempt=10, time=2000):
        """滑动到某个组件"""
        while attempt > 0:
            try:
                element = self.get_appium_driver().find_element_by_name(name)
                return element
            except:
                attempt -= 1
                self.swipe_up(time=time)
        return None
        pass

    def run_function_in_scroll_list(self, scroll_list, class_name, method="print('scroll in the scroll_list')"):
        children = scroll_list.find_elements_by_class_name('android.widget.LinearLayout')
        count = 0
        first_child = scroll_list.find_elements_by_class_name('android.widget.LinearLayout')[0]
        while len(children) > 0:
            second_child = scroll_list.find_elements_by_class_name('android.widget.LinearLayout')[1]
            pre_page = self.driver.page_source
            # 处理第一个组件
            count += 1

            # 滑动第一个组件的距离
            self.driver.swipe(0, 0, 0, first_child.size['height'], 1000)

            children = scroll_list.find_elements_by_class_name('android.widget.LinearLayout')
            # 判断是否已经滑动到最后，并从第二个组件开始执行操作
            if pre_page == self.driver.page_source:
                for i in range(1, len(children)):
                    count += 1
                print(count)
                # 完了
                break
            else:
                # 第一个组件已经消失了，第二个自动成为了第一个
                first_child = second_child
            pass

        pass
