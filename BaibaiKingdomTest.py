import unittest
from appium import webdriver
from zxz.zxz_utils import UiHelper
from baibai.baibai_operation import BaiBai_App
from selenium.webdriver.common.by import By
from time import sleep


class KingdomTest(unittest.TestCase):
    """拜拜王国测试"""

    def setUp(self):
        self.helper = UiHelper()
        self.driver = self.helper.get_appium_driver()
        self.app = BaiBai_App(self.driver, self.helper)
        self.app.input_account_password('10521397022', '123456')
        pass

    def tearDown(self):
        # self.app.exit_app()
        self.driver.quit()
        pass

    def test_001_(self):
        # 进入拜拜王国
        index_title_box = self.driver.find_elements_by_class_name('android.support.v7.widget.RecyclerView')
        # indexTitleBox = self.driver.find_elements(By.CLASS_NAME, 'android.support.v7.widget.RecyclerView')
        kingdom_entry = index_title_box[1].find_elements_by_class_name('android.widget.LinearLayout')
        kingdom_entry[0].click()
        self.driver.wait_activity('.view.activity.game.GameHomActivity', 30)
        self.assertEqual('.view.activity.game.GameHomActivity', self.driver.current_activity)

        # 进入基督
        l = self.driver.find_elements_by_class_name('android.support.v7.widget.RecyclerView')[1]\
            .find_elements_by_class_name('android.widget.LinearLayout')
        l[1].click()
        self.driver.wait_activity('.view.activity.game.GameTypeActivity', 30)
        search_list = self.driver.find_element_by_id('com.baibai.baibai:id/rv_search_list')

        # 处理
        # children = search_list.find_elements_by_class_name('android.widget.LinearLayout')
        # count = 0
        # first_child = search_list.find_elements_by_class_name('android.widget.LinearLayout')[0]
        # while len(children) > 0:
        #     second_child = search_list.find_elements_by_class_name('android.widget.LinearLayout')[1]
        #     pre_page = self.driver.page_source
        #     # 处理第一个组件
        #     count += 1
        #     # 滑动第一个组件的距离
        #     self.driver.swipe(0, 0, 0, first_child.size['height'], 1000)
        #
        #     children = search_list.find_elements_by_class_name('android.widget.LinearLayout')
        #     # 判断是否已经滑动到最后，并从第二个组件开始执行操作
        #     if pre_page == self.driver.page_source:
        #         for i in range(1, len(children)):
        #             count += 1
        #         print(count)
        #         # 完了
        #         break
        #     else:
        #         # 第一个组件已经消失了，第二个自动成为了第一个
        #         first_child = second_child
        #     pass
        start_x = search_list.location['x']
        start_y = search_list.location['y']
        elements = self.helper.find_elements_in_scroll_list(search_list, 'android.widget.LinearLayout')
        print(start_x, start_y)
        self.helper.swipe_to_top()
    pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KingdomTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
