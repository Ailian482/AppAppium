import time

class AppLogout(object):
    def __init__(self, driver):
        self.driver = driver

    def appLogout(self):
        self.driver.implicitly_wait(60)
        # 点击 我的 按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
        time.sleep(2)
        # 点击 个人主页 的设置齿轮按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/setting").click()
        # 点击 退出当前账号 按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvLogout").click()
        # 点击 确定
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/bt_positive").click()
        time.sleep(2)