from appium import webdriver
import unittest
import os
import time


class AndroidTests(unittest.TestCase):
    # 初始化一个driver
    def setUp(self) -> None:
        desired_caps = {}  # 定义一个空字典，用来存放参数和值，下面的参数名和参数值不能有错
        desired_caps["platformName"] = "Android"    # 平台名称，苹果用 iSO 表示
        desired_caps["platformVersion"] = "5.1"   # 手机版本号与用来测试的手机的版本号要一致
        desired_caps["deviceName"] = "Android Emulator"  # 设备名称，没有强行验证，有这个参数和值就行了
        desired_caps["noReset"] = "True"   # 不重置APP的数据，即每次跑完退出不重置数据，不用重新进入欢迎导航或者选择页面，直接进入App界面
        desired_caps["appPackage"] = "cn.xiaochuankeji.tieba"   # app包名，是手机用来区分APP的唯一标志
        desired_caps["appActivity"] = ".ui.base.SplashActivity"  # 界面，一个Activity就是一个界面

        # (获取Activity的方法：在cmd下输入adb shell dumpsys activity top|find "ACTIVITY"，然后点开App，cmd窗口立马回车)
        # C:\Users\Administrator>adb shell dumpsys activity top|find "ACTIVITY"
        #   ACTIVITY cn.xiaochuankeji.tieba/.ui.base.SplashActivity 1fd0df1b pid=837
        #  "cn.xiaochuankeji.tieba"是包名，".ui.base.SplashActivity"是
        # 把获取到的两个值，分别添加到"appPackage"和"appActivity"上
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # 这里写的是请求服务器地址，也就是Appium开始界面的host和port一样

    def tearDown(self) -> None:
        self.driver.quit()

    def test_elements_by_id_02(self):
        '''通过find_elements_by_id获取"视频"、"我的"控件，并点击它们'''
        self.driver.implicitly_wait(60)
        el1 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        # 获取当前页面id为"cn.xiaochuankeji.tieba:id/title"的所有控件，并放在列表中，通过下标获取要操作的控件
        # demo3
        print(el1[2].text)  # 获取“视频”控件，打印其文本
        el1[2].click()  # 获取“视频”控件，并点击它
        # demo4
        el2 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/textTabItem")
        print(el2[3].text)  # 获取“我的”控件，打印其文本
        el2[2].click()  # 获取“我的”控件，并点击它


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

