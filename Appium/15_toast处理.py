from appium import webdriver
import time
import unittest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""
场景：评论帖子的时候，点击发送，提示”评论发送成功“的提示黑框很快消失，这种就是toast，用uiautomator是定位不到的
测试中要想获取toast的内容，需要在初始化的时候添加一个 automationName 参数，值为 Uiautomator2
Appium 1.6.3 版本开始，Appium才支持对toast的处理
为什么是Uiautomator2呢？
因为Appium 1.6.3之前封装的是Uiautomator，1.6.3版本之后才封装了支持对toast处理的Uiautomator2
"""

class AndroidTest(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'  # 不重置APP
        desired_caps['fullReset'] = 'True'  # 每次跑完把App卸载，把所有数据清除掉
        desired_caps['app'] = 'E:/test/zuiyou518.apk'  # app安装包的路径加安装包名称
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['automationName'] = 'Uiautomator2'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self) -> None:
        pass

    def test_toast(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(10)
        # 点击帖子的评论按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/middle_view").click()
        time.sleep(3)
        # 在评论输入框中输入"哈哈哈"
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys("哈哈哈")
        # 点击发送按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        # 用显示等待时间，等待toast框出现，然后获取其文本内容
        ele = WebDriverWait(self.driver, 20, 0.2).until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(@text, '评论发送成功')]")))
        # toast_t = ("xpath", ".//*[contains(@text, '评论发送成功')]")
        # ele = WebDriverWait(self.driver, 20, 0.2).until(EC.presence_of_element_located(toast_t))
        print(ele.text)
        time.sleep(2)
        self.driver.keyevent(4)
        self.driver.find_elements(By.ID)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

