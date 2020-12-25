from appium import webdriver
import time
import unittest
import os

"""
App中要实现每条测试用例都要独立的话，简单粗暴的方法是，每跑完一条用例就把App卸载重新安装
实现卸载和安装的方法是在初始化的时候添加两个参数：fullReset 和 app
如果项目的数据之间的依赖关系太强了，就需要重置App，如果不是很强，那么就没必要重置App
如果项目的业务需要在某个地方新建数据，然后用到别的界面中，那么可以把新建数据以及使用数据都写在一个用例里面
有些App安装完第一次进去的时候需要选择一些东西或者有导航的，那么可以把这些东西封装到public的公用方法里，每次安装打开，直接调用
"""
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AndroidTest(unittest.TestCase):
    def setUp(self) -> None:

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['fullReset'] = 'True'  # 每次跑完把App卸载，把所有数据清除掉
        desired_caps['app'] = 'E:/test/zuiyou518.apk'  # app安装包的路径加安装包名称
        # desired_caps['app'] = PATH('E:/test/zuiyou518.apk')
        # desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_01(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        time.sleep(2)
        # 点击 我的 按钮
        self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/textTabItem")[3].click()
        # 点击 立即登录/注册 按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").click()
        # 点击 密码登录
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login_mode").click()
        # 输入手机号
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/phone_num_edit").send_keys("15127409611")
        # 输入密码
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/code_edit").send_keys("a123456")
        # 点击登录
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()

    def test_login_02(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        time.sleep(2)
        # 点击 我的 按钮
        self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/textTabItem")[3].click()
        # 点击 立即登录/注册 按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").click()
        # 点击 密码登录
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login_mode").click()
        # 输入手机号
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/phone_num_edit").send_keys("15127409611")
        # 输入密码
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/code_edit").send_keys("a123456")
        # 点击登录
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)