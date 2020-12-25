from appium import webdriver
import time
import unittest
import os
from ZuiyouApp0test.public.Applogout import AppLogout
from ZuiyouApp0test.public.Checklogin import CheckLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AndroidLogin(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "5.1.1"
        desired_caps["deviceName"] = "Android Emulator"
        desired_caps["noReset"] = "True"
        desired_caps["appPackage"] = "cn.xiaochuankeji.tieba"
        desired_caps["appActivity"] = ".ui.base.SplashActivity"
        desired_caps["automationName"] = "Uiautomator2"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        time.sleep(2)
        print("startTime:" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))

    def tearDown(self) -> None:
        filedir = "E:/test/Androidscr/"
        if not os.path.exists(filedir):
            os.mkdir(os.path.join("E:/", "test", "Androidscr"))
        print("endTime:" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
        screen_name = filedir + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()  # 关闭App

    def testlogin01_01(self):
        '''输入10位错误的手机号进行登录'''
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item")
        except:
            pass
        # 调用检测APP登录状态方法，并填入登录信息
        CheckLogin(self.driver).checkLogin("1512740961", "a123456")
        # 点击登录
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()
        time.sleep(1)
        # 获取toast提示信息
        el_toast = WebDriverWait(self.driver, 20, 0.2).until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(@text, '手机号还没有注册')]")
        ))
        print(el_toast.text)
        # 断言
        self.assertEqual("手机号还没有注册", el_toast.text)

    def testlogin01_02(self):
        '''输入11位未注册的手机号进行登录'''
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item")
        except:
            pass
        # 调用检测APP登录状态方法，并填入登录信息
        CheckLogin(self.driver).checkLogin("15055119623", "a123456")
        # 点击登录
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()
        time.sleep(1)
        # 获取toast提示信息
        el_toast = WebDriverWait(self.driver, 20, 0.2).until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(@text, '手机号还没有注册')]")
        ))
        print(el_toast.text)
        # 断言
        self.assertEqual("手机号还没有注册", el_toast.text)

    def testlogin01_03(self):
        '''不输入手机号'''
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item")
        except:
            pass
        # 调用检测APP登录状态方法，并填入登录信息
        CheckLogin(self.driver).checkLogin("", "a123456")
        # 断言“登录”按钮不可用
        login_bool = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").is_enabled()
        self.assertFalse(login_bool)

    def testlogin01_04(self):
        '''输入错误的密码进行登录'''
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item")
        except:
            pass
        # 调用检测APP登录状态方法，并填入登录信息
        CheckLogin(self.driver).checkLogin("15127409611", "123456")
        # 点击登录
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()
        time.sleep(1)
        # 获取toast提示信息
        el_toast = WebDriverWait(self.driver, 20, 0.2).until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(@text, '账号或密码错误')]")
        ))
        print(el_toast.text)
        # 断言
        self.assertEqual("账号或密码错误", el_toast.text)

    def testlogin01_05(self):
        '''不输入密码'''
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item")
        except:
            pass
        # 调用检测APP登录状态方法，并填入登录信息
        CheckLogin(self.driver).checkLogin("15127409611", "")
        # 断言“登录”按钮不可用
        login_bool = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").is_enabled()
        self.assertFalse(login_bool)

    def testlogin01_06(self):
        '''输入正确的手机号和密码进行登录'''
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item")
        except:
            pass
        # 调用检测APP登录状态方法，并填入登录信息
        CheckLogin(self.driver).checkLogin("15127409611", "a123456")
        # 点击登录
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()
        time.sleep(1)
        # 跳转到个人主页
        zan_text = self.driver.find_element_by_xpath("//android.widget.TextView[@text='获赞']").text
        guan_text = self.driver.find_element_by_xpath("//android.widget.TextView[@text='关注']").text
        fen_text = self.driver.find_element_by_xpath(("//android.widget.TextView[@text='粉丝']")).text
        # 退出登录
        AppLogout(self.driver).appLogout()
        # 断言
        self.assertEqual(zan_text, "获赞")
        self.assertEqual(guan_text, "关注")
        self.assertEqual(fen_text, "粉丝")


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(AndroidLogin)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
