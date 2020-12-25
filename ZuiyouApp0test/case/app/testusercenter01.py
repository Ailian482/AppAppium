from appium import webdriver
import time
import unittest
import os
from ZuiyouApp0test.public.Entrypersonal import EnterPer

class AndroidShouye(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "5.1.1"
        desired_caps["deviceName"] = "Android Emulator"
        desired_caps["noReset"] = "True"
        desired_caps["appPackage"] = "cn.xiaochuankeji.tieba"
        desired_caps["appActivity"] = ".ui.base.SplashActivity"
        desired_caps["automationName"] = "Uiautomator2"
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

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

    def testpersonal01_13(self):
        '''是否能在用户个人主页正常关注或取关其他用户'''
        # 调用进入第一条帖子贴主的个人主页EnterPer().enterPer()
        EnterPer(self.driver).enterPer()
        # 获取贴主昵称
        user_name = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/member_name").text
        # 定位 +关注/已关注按钮
        guanzhu = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_follow")
        old_guanzhu_text = guanzhu.text
        if old_guanzhu_text == "+ 关注":  # 如果列表第一个贴主为 未关注
            # 点击“+关注“按钮
            guanzhu.click()
            new_guanzhu_text = guanzhu.text
            # 返回上一页页面
            self.driver.keyevent(4)
            time.sleep(2)
            # 进入我的个人主页，获取我关注的用户昵称
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
            time.sleep(2)
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/follow").click()
            time.sleep(2)
            eles = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/tv_name")
            userList = []
            for i in range(0, len(eles)):
                userList.append(eles[i].text)
            allUserList = "".join(userList)
            # 断言
            self.assertEqual("已关注", new_guanzhu_text)
            self.assertIn(user_name, allUserList)

        elif old_guanzhu_text == "已关注":  # 如果列表第一个贴主为 已关注
            # 点击“已关注”按钮
            guanzhu.click()
            # 弹出提示框，点击确定
            tishi = self.driver.find_element_by_xpath("//*[@text='确定取消关注吗？']")
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/bt_positive").click()
            new_guanzhu_text = guanzhu.text
            # 返回上一页页面
            self.driver.keyevent(4)
            time.sleep(2)
            # 进入我的个人主页，获取我关注的用户昵称
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
            time.sleep(2)
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/follow").click()
            time.sleep(2)
            eles = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/tv_name")
            userList = []
            for i in range(0, len(eles)):
                userList.append(eles[i].text)
            allUserList = "".join(userList)
            # 断言
            self.assertEqual("+ 关注", new_guanzhu_text)
            self.assertNotIn(user_name, allUserList)

    def testpersonal01_14(self):
        '''是否可以私聊其他用户'''
        EnterPer(self.driver).enterPer()
        # 获取贴主昵称
        user_name1 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/member_name").text
        # 定位 私聊，点击
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_chat").click()
        time.sleep(2)
        # 跳转到私聊页面，获取私聊页面信息
        user_name2 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title").text
        default = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/input").text
        fs = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/text").text
        # AppLogout(self.driver).appLogout()  # 退出登录
        # 断言
        self.assertEqual(user_name1, user_name2)
        self.assertEqual("说点好听的...", default)
        self.assertEqual("发送", fs)

    def testpersonal01_15(self):
        '''是否可以与用户正常私聊'''
        EnterPer(self.driver).enterPer()
        # 定位 私聊，点击
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_chat").click()
        time.sleep(2)
        # 输入私聊内容
        inputt = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/input")
        inputt.send_keys("这是一条Test" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
        old_input = inputt.text   # 获取输入的内容
        # 发送
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/text").click()
        time.sleep(1)
        # 获取聊天框的内容
        eles = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/content")
        contentRawList = []
        for i in range(0, len(eles)):
            contentRawList.append(eles[i].text)
        all_contentRawList = "".join(contentRawList)
        # 断言
        self.assertIn(old_input, all_contentRawList)


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(AndroidShouye)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
