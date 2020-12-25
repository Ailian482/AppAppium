from ZuiyouApp0test.public.Enterpage import EnterPage
from ZuiyouApp0test.public.Applogout import AppLogout
import time

class CheckLogin(object):
    def __init__(self, driver):
        self.driver = driver

    def checkLogin(self, phone, passwd):
        try:
            self.driver.implicitly_wait(60)
            # 点击 我的 按钮
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
            ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").is_displayed()
            if ele == True:
                # 调用进入Enterpage的进入登录界面enterLogin()方法
                EnterPage(self.driver).enterLogin(phone, passwd)


        except:
            AppLogout(self.driver).appLogout()  # 如果APP登录了，那么就要先退出
            # 调用进入Enterpage的进入登录界面enterLogin()方法
            EnterPage(self.driver).enterLogin(phone, passwd)