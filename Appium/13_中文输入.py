from appium import webdriver
import time
import unittest

class AndroidTest(unittest.TestCase):
    def setUp(self) -> None:
        # 输入中文需要添加两个参数：
        #   unicodeKeyboard（在手机安装一个Appium输入法）
        #   resetKeyboard（重置键盘，把Appium输入法作为默认输入法）
        # 注意：Appium输入法是没有键盘的，如果后续要做功能测试输入，需要到手机设置把输入法调回来

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_zhongwen(self):
        self.driver.implicitly_wait(60)
        # 点击搜索按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(2)
        # 输入搜索内容“小草”
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("小草")
        self.driver.keyevent(84)  # 搜索

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)