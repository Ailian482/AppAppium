from appium import webdriver
import unittest
import time

class AndroidTests(unittest.TestCase):
    # 初始化一个driver
    def setUp(self) -> None:
        desired_caps = {}  # 定义一个空字典，用来存放参数和值，下面的参数名和参数值不能有错
        desired_caps["platformName"] = "Android"    # 平台名称，苹果用 iSO 表示
        desired_caps["platformVersion"] = "5.1"   # 手机版本号与用来测试的手机的版本号要一致
        desired_caps["deviceName"] = "Android Emulator"  # 设备名称，没有强行验证，有这个参数和值就行了
        desired_caps["noReset"] = "True"   # 不重置APP的数据，每次跑完退出不重置数据，不用重新进入欢迎或者选择页面，直接进入App界面
        desired_caps["appPackage"] = "cn.xiaochuankeji.tieba"   # app包名，是手机用来区分APP的唯一标志
        desired_caps["appActivity"] = ".ui.base.SplashActivity"  # App第一个界面，一个Activity就是一个界面

        # (获取第一个Activity的方法：在cmd下输入adb shell dumpsys activity top|find "ACTIVITY"，然后点开App，cmd窗口立马回车)
        # C:\Users\Administrator>adb shell dumpsys activity top|find "ACTIVITY"
        #   ACTIVITY cn.xiaochuankeji.tieba/.ui.base.SplashActivity 1fd0df1b pid=837
        #  "cn.xiaochuankeji.tieba"是包名，".ui.base.SplashActivity"是第一个Activity
        # 把获取到的两个值，分别添加到"appPackage"和"appActivity"上
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # 这里写的是请求服务器地址，端口要和Appium开始界面的port一样

    def tearDown(self) -> None:
        self.driver.quit()

    def test_element_by_id_01(self):
        '''通过find_element_by_id获取"关注"、"最右"控件，并点击它们'''
        self.driver.implicitly_wait(60)  # 隐式等待60s
        # demo1
        ele1 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")  # 获取“关注”控件
        # 控件属性值是从sdk\tools目录下的uiautomatorviewer.bat上面获取的
        # 打开uiautomatorviewer.bat后，点击左上角的Device Screenshot(uiautomator dump) 按钮，获取Activity
        print(ele1.text)  # 打印控件文本
        ele1.click()  # 点击它
        time.sleep(2)
        # demo 2
        ele2 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/textTabItem") # 获取“最右”控件
        print(ele2.text)
        ele2.click()
        time.sleep(2)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)  # verbosity:表示测试结果的信息复杂度