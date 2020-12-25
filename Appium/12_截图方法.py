from appium import webdriver
import time
import unittest
import os

class AndroidTest(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_get_screenshot(self):
        '''截图方法和Web自动化一样'''
        self.driver.implicitly_wait(60)

        # 点击图文按钮
        self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")[3].click()
        time.sleep(2)
        # 截图
        # filedir = "E:/test/screenshot1/"
        # if not os.path.exists(filedir):
        #     os.makedirs(os.path.join("E:/", "test", "screentshot1"))
        # filename = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file('E:/test/screentshot1/test1.png')

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)