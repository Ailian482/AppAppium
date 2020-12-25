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

    def test_click(self):  # click()方法 -- 点击
        '''点击搜索按钮'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(3)
        # 定位点击搜索按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()

    def test_send_keys(self):  # send_keys()方法 -- 输入，App中，只能作用在 输入框（class属性值是"android.widget.EditText"）
        '''进入搜索页面，并在搜索框输入“abc”'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(3)
        # 定位点击搜索按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        # 定位输入框，输入“abc”
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys('abc')

    def test_text_clear(self):
        '''获取在输入框输入的文本信息'''
        # .text 方法 -- 获取控件上的信息，一般做App自动化，在输入框输入内容后，要检查输入的内容是否正确，此时可以用.text方法去验证
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(3)
        # 定位点击搜索按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(2)
        # 定位输入框
        ele = self.driver.find_element_by_class_name("android.widget.EditText")
        ele.send_keys('123')  # 输入“123”
        time.sleep(1)
        print(ele.text)  # 打印获取到输入框输入的 内容
        # 清空输入框
        ele.clear()

    def test_get_window_size(self):  # get_window_size() 方法 -- 获取手机屏幕分辨率，返回的是一个字典
        '''获取手机屏幕分辨率'''
        size = self.driver.get_window_size()
        print(size)
        height = size["height"]
        width = size["width"]
        print("此手机的屏幕分辩率是：", str(height)+"*"+str(width))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
