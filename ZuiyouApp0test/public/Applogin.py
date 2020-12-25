import time

class AppLogin(object):
    def __init__(self, driver):
        self.driver = driver

    def appLogin(self):
        try:
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvConfirmWithBg").click()
        except:
            pass
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()  # 点击 我的 按钮
        time.sleep(1)
        # 点击 立即登录/注册 按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").click()
        time.sleep(1)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login_mode").click()  # 点击 密码登录
        time.sleep(2)
        # 输入手机号
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/phone_num_edit").send_keys("15127409611")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/code_edit").send_keys("a123456")  # 输入密码
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()  # 点击登录
        time.sleep(5)