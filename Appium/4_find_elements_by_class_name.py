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
        pass
    """
    当前页面要定位的控件class属性不是唯一的或者同类型的class属性不是第一个，用find_elements_by_class_name("属性值")，
    会找到class属性相同的所有控件，并放到一个列表中，可以通过下标获取定位你要的控件
    如何获取TextView类型控件的下标呢？
    可以通过一个for循环去调试，每循环一次就打印下标和控件文本信息，通过打印出来的信息可以拿到要定位控件的下标
    如果要定位的控件是图片（ImageView类型），那么只能通过dom树形结构去找，数树形结构的时候，一定要把它展开
    """
    def test_elements_by_class_name_04(self):
        '''定位TextView类型控件'''
        self.driver.implicitly_wait(60)
        self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(3)
        # 找到所有class属性值为“android.widget.TextView”的控件，并放到一个列表中
        ele = self.driver.find_elements_by_class_name("android.widget.TextView")
        # 通过for循环调试，找到要定位控件的文本，及其对应的下标
        for i in range(0,len(ele)):
            print('这是第%d个控件：' % i + ele[i].text)
        # 通过下标对控件进行相应的操作
        print("===============================")
        ele1 = ele[5]
        print(ele1.text)
        print("===============================")
        ele2 = ele[9]
        print(ele2.text)

    def test_elements_by_class_name_05(self):
        """定位ImageView类型控件"""
        self.driver.implicitly_wait(60)
        self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        time.sleep(5)
        # 只能通过dom树形来数控件是界面中的第几个
        # 定位“动态”按钮上的星星图标，并点击它
        ele = self.driver.find_elements_by_class_name("android.widget.ImageView")
        ele[19].click()

    def test_element_by_class_name_06(self):
        """定位搜索按钮，并点击它"""
        self.driver.implicitly_wait(60)  # 隐式等待
        self.driver.find_element_by_class_name("android.widget.TextView")
        time.sleep(3)  # 强制等待界面所有控件都加载出来
        ele = self.driver.find_elements_by_class_name('android.widget.ImageView')
        ele1 = ele[3]
        ele1.click()  # 点击

    def test_element_by_class_name_07(self):
        """点击搜索按钮，进入搜索界面，并点击地第二条热门话题"""
        self.driver.implicitly_wait(60)  # 隐式等待
        self.driver.find_element_by_class_name("android.widget.TextView")
        time.sleep(3)  # 强制等待界面所有控件都加载出来
        # 定位并点击搜索按钮
        ele = self.driver.find_elements_by_class_name('android.widget.ImageView')
        ele1 = ele[3]
        ele1.click()
        # 找到所有相同class属性的控件
        aa = self.driver.find_elements_by_class_name("android.widget.TextView")
        bb = aa[4]  # 定位到第2条热门话题
        cc = bb.text
        print(cc)
        bb.click()  # 点击它
        self.assertEqual("超可爱的圣诞头像", cc)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)