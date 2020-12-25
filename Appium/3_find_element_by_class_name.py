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

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self) -> None:
        self.driver.quit()

    """
    App自动化的class属性和Web自动化的class属性不太一样，
    在App自动化中，class是一种属性，但class属性值是更像是Web自动化的标签类型（控件类型），
    在Android中，大部分的控件都是放在"android.widget." 下，
    后面的值表示不同类型的控件，比如：android.widget.ImageView(图标控件)、android.widget.TextView(文本控件)、
    android.widget.EditText(输入框)、android.widget.RelativeLayout、android.widget.LinearLayout等
    """
    def test_element_by_class_name_03(self):
        self.driver.implicitly_wait(60)  # 隐式等待
        self.driver.find_element_by_class_name("android.widget.TextView")
        time.sleep(3)  # 强制等待界面所有控件都加载出来
        # 只能用来定位，当前界面只有一个相同类型的class属性或者是同类型class属性的第一个
        # 我们可以通过控件的dom树形坐标知道他是不是同类型class属性的第一个，从上到下纵坐标增大，从左到右横坐标在增大
        # 点击第一个TextView类型控件
        ele = self.driver.find_element_by_class_name('android.widget.TextView')
        ele.click()
        time.sleep(2)



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
