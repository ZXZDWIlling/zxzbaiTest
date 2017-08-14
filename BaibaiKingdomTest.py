import unittest
from appium import webdriver
from zxz.zxz_utils import UiHelper
from baibai.baibai_operation import BaiBai_App

class KingdomTest(unittest.TestCase):
    '''拜拜王国测试'''

    def setUp(self):
        self.helper = UiHelper()
        self.driver = self.helper.getWebDriver()
        self.app = BaiBai_App(self.driver, self.helper)
        self.app.input_account_password('05521397022', '123456')
        pass

    def tearDown(self):
        self.app.exit_app()
        self.driver.quit()
        pass

    def test_001_(self):
        # 进入拜拜王国
        indexTitleBox = self.driver.find_elements_by_class_name('android.support.v7.widget.RecyclerView')
        kingdomEntry = indexTitleBox[1].find_elements_by_class_name('android.widget.LinearLayout')
        kingdomEntry[0].click()
        self.driver.wait_activity('.view.activity.game.GameHomActivity', 30)
        self.assertEqual('.view.activity.game.GameHomActivity', self.driver.current_activity)

        # 进入基督



        pass

    pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KingdomTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
