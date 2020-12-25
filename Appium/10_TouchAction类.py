from appium import webdriver
import time
import unittest
from appium.webdriver.common.touch_action import TouchAction

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

    def test_TouchAction(self):
        self.driver.implicitly_wait(60)
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(3)
        # TouchAction类的方法都是要.perform()方法去实现
        # 1. TouchAction().tap(控件定位) -- 控件点击
        TouchAction(self.driver).tap(ele).perform()
        time.sleep(2)
        # 2. TouchAction().tap(坐标) -- 坐标点击
        TouchAction(self.driver).tap(x=300, y=60).perform()
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        TouchAction(self.driver).tap(x=width*0.416, y=height*0.047)

        # 3. press某个点（最右），然后释放
        TouchAction(self.driver).press(x=80, y=1228).release().perform()

        # 4. 长按某个点（最右）
        TouchAction(self.driver).long_press(x=80, y=1228, duration=3000).release().perform()

        # 5. 长按某个控件（我的）
        e = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/textTabItem")[3]
        TouchAction(self.driver).long_press(e).release().perform()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)