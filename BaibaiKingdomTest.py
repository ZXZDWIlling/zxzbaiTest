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
        self.app.input_account_password('05521397022', '123456')
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
        # elements = self.helper.find_elements_in_scroll_list(search_list, 'android.widget.LinearLayout')
        # print(start_x, start_y)
        for i in self.helper.run(search_list, 'android.widget.LinearLayout'):
            i.click()
            sleep(10)
            self.driver.press_keycode('4')
    pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KingdomTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
