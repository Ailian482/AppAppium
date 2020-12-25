import time

class EnterPer(object):
    def __init__(self, driver):
        self.driver = driver

    def enterPer(self):
        # 调用登录方法
        # AppLogin(self.driver).appLogin()
        self.driver.implicitly_wait(60)
        # 点击最右
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        time.sleep(2)
        # 进入第一条帖子贴主的个人主页
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/avatar_view_avatar").click()
        time.sleep(2)

