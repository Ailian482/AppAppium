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

    def test_swipe(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(3)
        # 实现页面的一些动作 ，坐标从左到右变大，从上到下变大
        # .swipe(x1, y1, x2, y2, t)
        # x1, y1分别是初始坐标的横纵坐标，x2, y2分别是终点坐标的横纵坐标，t表示持续时间（实现这个动作的时间），单位为毫秒
        # 1. 实现页面从下往上滑--上滑
        self.driver.swipe(350, 1000, 350, 200, 3000)
        time.sleep(1)
        # 2. 实现页面从上往下滑--下拉
        self.driver.swipe(350, 200, 350, 1000, 3000)
        time.sleep(1)
        # 3. 实现页面从右往左滑动--左滑
        self.driver.swipe(500, 500, 100, 500, 3000)
        time.sleep(1)
        # 4. 实现页面从左往右滑动--右滑
        self.driver.swipe(100, 800, 500, 800, 3000)
        time.sleep(1)
        # 5. 实现点击
        self.driver.swipe(500, 200, 500, 200, 100)  # 在屏幕某个坐标上持续时间很短
        # 6. 实现长按
        self.driver.swipe(500, 200, 500, 200, 3000)  # 在屏幕某个坐标上持续时间较长

        # **重要：通过获取初始坐标和终点坐标在手机屏幕分辨率上的四个比例，可以灵活用到不同屏幕分辨率的手机上，实现页面滑动
        # 通过页面中的某些控件的布局（bounds）进行比例调试
        # 获取手机屏幕分辨率
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        # 在不同手机屏幕分辨率下通过比例实例滑动，下面是下拉动作，其他动作方法类似
        self.driver.swipe(width*0.625, height*0.165, width*0.625, height*0.855, 3000)



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)