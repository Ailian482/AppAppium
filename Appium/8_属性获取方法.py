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

    def test_get_attribute(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(3)
        # 进入到 我的 界面
        ele = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/textTabItem")
        ele[3].click()
        # 1. 获取当前（“我的”）页面的Activity信息:.current_activity
        print(self.driver.current_activity)
        # 2. 获取“我的”控件的属性值:.get_attribute("属性名")
        print(ele[3].get_attribute("className"))
        print(ele[3].get_attribute("resourceId"))
        # 3. 判断“我的”控件是否显示，返回布尔值:.is_displayed()
        print(ele[3].is_displayed())
        # 4. 判断“我的”控件是否可用，返回布尔值:.is_enabled()
        print(ele[3].is_enabled())


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)