from appium import webdriver
import time
import unittest

class AndroidTest(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_keyevent(self):
        """Android keycode安卓的一些按键"""
        """常用的几个按键：
        KEYCODE_MENU 菜单键82
        KEYCODE_BACK 返回键4
        KEYCODE_SEARCH 搜索键84
        KEYCODE_ENTER 回车键66
        KEYCODE_DEL 退格键67
        后续需要用其他按键可以在百度搜索Android keycode"""
        self.driver.implicitly_wait(60)
        # 定位搜索按钮
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b")
        ele.click()  # 点击它
        # 安卓按键的使用方法，直接传对应按键的数值到keyevent()里面即可
        # 定位搜索输入框，并输入 Ailian
        input = self.driver.find_element_by_class_name("android.widget.EditText").send_keys("Ailian")
        self.driver.keyevent(84)  # 搜索
        time.sleep(2)
        self.driver.keyevent(4)  # 返回
        time.sleep(2)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)