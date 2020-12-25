from appium import webdriver
import time
import unittest
import os
from ZuiyouApp0test.public.Checklogin import CheckLogin
from ZuiyouApp0test.public.Applogin import AppLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

    def testshouye01_08(self):
        '''检查首页导航栏文案显示是否正常'''
        # 调用登录方法
        CheckLogin(self.driver).checkLogin("15127409611", "a123456")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()  # 点击登录
        time.sleep(5)
        # 点击最右
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        self.driver.implicitly_wait(60)
        # 定位导航按钮
        guanzhu_text = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title").text
        tuijian_text = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")[1].text
        shipin_text = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")[2].text
        tuwen_text = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")[3].text
        # AppLogout(self.driver).appLogout()  # 退出登录
        # 断言
        self.assertEqual("关注", guanzhu_text)
        self.assertEqual("推荐", tuijian_text)
        self.assertEqual("视频", shipin_text)
        self.assertEqual("图文", tuwen_text)

    def testshouye01_09(self):
        '''帖子列表分享到站内右友时留言是否正确'''
        # 调用登录方法
        # AppLogin(self.driver).appLogin()
        self.driver.implicitly_wait(60)
        # 点击最右
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(2)
        # 获取第一条帖子的点击帖子列表第一条帖子的分享按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/operate_share").click()
        # 点击站内右友
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ivIcon").click()
        # 点击 我的关注
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/rl_my_follow").click()
        # 获取第一个用户昵称，并选择它
        user = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_name")
        user_name1 = user.text
        user.click()
        # 定位留言框，并输入留言
        ly = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/et_share_message")
        ly.send_keys("hi" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
        # 获取留言框的内容
        ly_text1 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/et_share_message").text
        # 点击发送
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_send").click()
        # 跳转到聊天框，获取右友昵称
        user_name2 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title").text
        # 获取帖子的
        # 获取转发的留言内容
        ly_text = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/content")
        ly_textRawLlist = []
        for i in range(0, len(ly_text)):
            ly_textRawLlist.append(ly_text[i].text)
        ly_textList = "".join(ly_textRawLlist)
        # AppLogout(self.driver).appLogout()  # 退出登录
        # 断言
        self.assertEqual(user_name1, user_name2)
        self.assertIn(ly_text1, ly_textList)

    def testshouye01_10(self):
        '''帖子列表内容跳转是否正确'''
        #调用登录方法
        # AppLogin(self.driver).appLogin()
        self.driver.implicitly_wait(60)
        # 点击最右
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(2)
        # 定位获取第一条帖子的信息
        user_name1 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/simple_member_tv_name").text
        a = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        old_content = a.text
        a.click()  # 点击帖子
        time.sleep(3)
        # 获取跳转后页面信息
        title = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTitle").text
        user_name2 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/post_head_name").text
        new_content = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvPostContent").text
        # AppLogout(self.driver).appLogout()  # 退出登录
        # 断言
        self.assertEqual("帖子详情", title)
        self.assertEqual(user_name1, user_name2)
        self.assertEqual(old_content, new_content)

    def testshouye01_11(self):
        '''帖子详情页评论功能是否正常'''
        #调用登录方法
        # AppLogin(self.driver).appLogin()
        self.driver.implicitly_wait(60)
        # 点击最右
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(2)
        # 进入第一条帖子的详情页
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view").click()
        # 定位评论框，输入内容
        pinglun = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput")
        pinglun.send_keys("这是一条Test" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
        Mypinglun = pinglun.text   # 获取我的评论内容
        print(Mypinglun)
        # 点击发送
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        # 获取toast框内容
        toast = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(@text, '评论发送成功')]")
        ))
        toast_text = toast.text
        print(toast_text)
        # 获取评论内容
        eles = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/expandTextView")
        contentList = []
        for i in range(0, len(eles)):
            contentList.append(eles[i].text)
        allcontentList = "".join(contentList)  # 把所有评论拼成一个字符串
        # AppLogout(self.driver).appLogout()  # 退出登录
        # 断言
        self.assertEqual("评论发送成功",toast_text)
        self.assertIn(Mypinglun, allcontentList)

    def testshouye01_12(self):
        '''点击个人头像是否可以正常进入贴主个人主页'''
        # 调用登录方法
        # AppLogin(self.driver).appLogin()
        self.driver.implicitly_wait(60)
        # 点击最右
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(2)
        # 获取第一条帖子贴主的昵称
        user_name1 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/simple_member_tv_name").text
        # 定位第一条帖子的个人头像，并点击它
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/avatar_view_avatar").click()
        # 进入贴主个人主页，获取页面信息
        title1 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_profile").text
        title2 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_zone").text
        user_name2 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/member_name").text
        sx = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/btn_chat").text
        # AppLogout(self.driver).appLogout()  # 退出登录
        # 断言
        self.assertEqual("主页", title1)
        self.assertEqual("空间", title2)
        self.assertEqual(user_name1, user_name2)
        self.assertEqual("私信", sx)


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(AndroidShouye)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()

