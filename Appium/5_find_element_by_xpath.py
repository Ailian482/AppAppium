from appium import webdriver
import time
import unittest
"""
xpath思想：从dom树形一层一层往下找
定位元素的时候，首先看控件类型，再看有什么属性
在App中，一般不用绝对路径写xpath路径，因为写起来太长了，一般用相对路径写xpath路径
语法结构和Web中的语法是一样的
"""
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
        pass

    def test_by_xpath_01(self):
        self.driver.implicitly_wait(60)  # 隐式等待
        self.driver.find_element_by_class_name("android.widget.TextView")
        time.sleep(3)  # 强制等待界面所有控件都加载出来

        # 1. xpath通过id查找单个元素（关注按钮），这种方法只能定位当前界面相同属性值唯一或者是同类型的第一个
        gz = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/title']")
        print(gz.text)
        gz.click()

        # 2. xpath通过id查找多个元素（定位发布话题按钮），找到一组id一样的控件
        # find_elements_by_xpath最后还要通过下标定位，太麻烦了了，所以尽量不要用这种方法
        ht = self.driver.find_elements_by_xpath("//android.widget.ImageView[@resource-id='cn.xiaochuankeji.tieba:id/topic']")
        ht[0].click()

        # 3. 如果要定位的控件没有id，但是有text属性，且其属性值在当前界面是唯一的
        # 可以通过text文本来定位，（定位动态按钮）
        dt = self.driver.find_element_by_xpath("//android.widget.TextView[@text='动态']")
        dt.click()

        # 4. 通过text属性定位无控件属性，不管控件是什么标签类型，只要属性值是我想要的就行
        sp = self.driver.find_element_by_xpath("//*[@text='视频']")
        sp.click()

        # 5. xpath通过class属性定位控件（搜索页面的输入框），这有点多此一举
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        input = self.driver.find_element_by_xpath("//android.widget.EditText[@class='android.widget.EditText']")
        input.click()

        # 6. 一个属性没有办法实现定位，那么可以通过多种属性用 and 连接起来实现定位
        # xpath通过id和text属性定位 视频 按钮
        tj = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/title' and @text='视频']")
        tj.click()

        # 7. 如果控件没有id和text属性，那么需要通过层级的方式定位，逐层往上找有特殊属性的级
        # 通过父级定位 消息 按钮
        xx = self.driver.find_element_by_xpath("//android.view.ViewGroup[@resource-id='cn.xiaochuankeji.tieba:id/msg_item']/android.widget.TextView[1]")
        xx.click()

        # 8. 通过祖父级定位个人头像
        tx = self.driver.find_element_by_xpath("//android.widget.FrameLayout[@resource-id='cn.xiaochuankeji.tieba:id/avatar']/android.view.ViewGroup/android.widget.ImageView[3]")
        tx.click()

        # 9. 通过祖父级定位图文按钮
        tw = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='cn.xiaochuankeji.tieba:id/title_container']/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.TextView")
        tw.click()

        # 10. 定位兄弟关系，如果同级兄弟没有特殊属性，那么可以通过有特殊属性的兄弟，定位到父级，在通过父级定位无特殊属性的子级
        # 定位消息按钮上的图标
        tb = self.driver.find_element_by_xpath("//android.widget.TextView[@text='消息']/../android.widget.ImageView")
        tb.click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)