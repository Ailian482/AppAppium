from selenium import webdriver
import unittest
import os
import time
# from ZuiyouApp0test.public.login import Mylogin
from ZuiyouApp0test.public.pagenew import NewPage
from ZuiyouApp0test.public.xuanting import MoveTo

"""
selenium 自动化测试框架的目录结构：
    case层：放的是自动化测试用例（app、web），
           一个.py文件就是一个项目的模块（可以细分），尽量让.py文件的行数不要太多，
           .py文件里面的一个test开头的方法对应一个自动化测试用例(手工测试用例)
    public层：放的是公用业务（常用的）模块的API
    report层：报告输出，呈现自动化执行结果是通过还是不通过
    Ven层：
    testrunner.py：批量运行所有case的（比如说有100个case，可以把100个case全部运行完）
"""
"""
unittest单元测试框架，一般包含但部分：
    ① setUp(初始化)，
    ② 以test开头的方法(其实就是用例)，
    ③ tearDown(清理、释放)
运行程序的时候，是按照上面的①②③的顺序来执行，即每执行一条测试用例，都会先打开浏览器，执行用例，然后关闭浏览器
"""

class TestShouye(unittest.TestCase):
    # 我们自己定义的TestShouye类，继承了unittest的TestCase类，TestCase类里面的方法，TestShouye类都可以用
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # self是类的一个实例化对象，self.driver相当于一个类的初始化变量，可以被这个类的其他方法所认识使用
        # 如果没有加self，只是driver变量，那么就是方法里面的一个局部变量，其他方法是不能认识和使用的
        self.driver.get('http://101.133.169.100/yuns/index.php/')  # 进入项目
        self.driver.maximize_window()  # 窗口最大化
        time.sleep(5)  # 休眠5秒钟
        # 打印开始时间：年-月-日 时:分:秒。strftime是格式化时间(大小写要求)，time.localtime(time.time())拿到当前的时间
        print("stratTimes:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self) -> None:
        filedir = "E:test/screenshot/"  # 电脑的一个路径
        if not os.path.exists(filedir):  # 如果电脑没有上面的路径，就会在电脑上创建这个路径
            os.makedirs(os.path.join('E:/', 'test', 'screenshot'))
        # 打印执行完成的时间，如果用例执行失败了，可以通过这个时间找到截图
        print("endTimes:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        # 定义一个文件路径及其名称，screen_name = E:test/screenshot/2020-12-18.png
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        # 执行完后截图：路径/名称，拿到最后截图可以看图查错
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()  # 关闭浏览器

    def testShouye01_01(self):
        '''测试首页导航文案显示是否正常'''
        # 定位控件
        hy_text = self.driver.find_element_by_xpath("//div[@class='top']/span")
        login_text = self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
        regis_text = self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")
        shouye_text = self.driver.find_element_by_css_selector("div.help>a:first-child")
        order_text = self.driver.find_element_by_css_selector("div.help>a:nth-child(2)")
        lianxi_text = self.driver.find_element_by_css_selector("div.help>a:nth-child(3)")

        # 断言结果，实际结果与预期结果对比
        self.assertEqual("亲，欢迎您来到云商系统商城！", hy_text.text)  # 断言控件文本内容是否与预期一致
        self.assertEqual("登录", login_text.text)
        self.assertEqual("免费注册", regis_text.text)
        self.assertEqual("首页", shouye_text.text)
        self.assertEqual("我的订单", order_text.text)
        self.assertEqual("联系客服", lianxi_text.text)


    def testShouye01_02(self):
        '''验证登录按钮是否有效，跳转是否正确'''
        # 调用pagenew模块的新页面方法
        NewPage(self.driver).c_newpage("div.login>a:nth-child(1)")
        # 跳转后页面显示内容
        # 定位控件
        noassent_text = self.driver.find_element_by_css_selector('div.reg_name>span:nth-child(1)')
        zhuce_text = self.driver.find_element_by_css_selector('div.reg_name>a:nth-child(2)')
        uslogin_text = self.driver.find_element_by_xpath("//div[@class='bname']/span")

        # 断言结果
        self.assertEqual("没有帐号", noassent_text.text)
        self.assertEqual("立即注册", zhuce_text.text)
        self.assertEqual("用户登录", uslogin_text.text)


    def testShouye01_03(self):
        '''验证免费注册按钮是否有效，跳转是否正确'''
        # 调用pagenew模块的新页面方法
        NewPage(self.driver).c_newpage("div.login>a:nth-child(3)")
        # 跳转后页面显示内容
        # 定位控件
        havassent_text = self.driver.find_element_by_css_selector("div.reg_name>span:nth-child(1)")
        gologin_text = self.driver.find_element_by_css_selector('div.reg_name>a:nth-child(2)')
        usregis_text = self.driver.find_element_by_css_selector('div.reg_bname>span')
        klogin_text = self.driver.find_element_by_css_selector('div.sub_frm2>h3')

        # 断言
        self.assertEqual(havassent_text.text, "已经有帐号")
        self.assertEqual(gologin_text.text, "立即登录")
        self.assertTrue(klogin_text.is_displayed())

    def testShouye01_04(self):
        '''验证未登录情况下验证我的订单按钮是否有效，跳转是否正确'''
        # 调用pagenew模块新页面方法
        NewPage(self.driver).p_newpage("//div[@class='help']/a[2]")
        # 定位控件
        noassent_text = self.driver.find_element_by_css_selector('div.reg_name>span:nth-child(1)')
        zhuce_text = self.driver.find_element_by_css_selector('div.reg_name>a:nth-child(2)')
        uslogin_text = self.driver.find_element_by_xpath("//div[@class='bname']/span")

        # 断言结果
        self.assertEqual("没有帐号", noassent_text.text)
        self.assertEqual("立即注册", zhuce_text.text)
        self.assertEqual("用户登录", uslogin_text.text)

    def testShouye01_05(self):
        '''未登录情况下未登录情况下联系客服按钮是否有效,页面跳转是否正确'''
        # 调用pagenew模块新页面方法
        NewPage(self.driver).p_newpage("//div[@class='help']/a[3]")
        # 定位控件
        contactus = self.driver.find_element_by_css_selector('div.nm>span')
        conphone = self.driver.find_element_by_xpath('//div[@class="con"]/p[1]')
        phone = self.driver.find_element_by_xpath('//div[@class="con"]/p[2]')
        emai = self.driver.find_element_by_xpath('//div[@class="con"]/p[3]')
        website = self.driver.find_element_by_xpath('//div[@class="con"]/p[4]')
        adress = self.driver.find_element_by_xpath('//div[@class="con"]/p[5]')

        # 断言
        self.assertEqual("联系我们", contactus.text)
        self.assertEqual("联系我们：我们的电话是：", conphone.text)
        self.assertEqual(phone.text, "15030000000")
        self.assertEqual(emai.text, "邮箱地址是：aaa@aaa.com    ")
        self.assertEqual(website.text, "我们的网址是：www.aaa.com    ")
        self.assertEqual(adress.text, "地址：山西太原AA街AA号")

    def testShouye01_06(self):
        '''验证搜索内容有时，是否能搜索到正确结果'''
        self.driver.find_element_by_css_selector("input.but1").send_keys("衬衫")  # 定位搜索框输入衬衫
        self.driver.find_element_by_css_selector("input.but2").click()  # 点击搜索
        time.sleep(2)
        # self.driver.refresh()  # 刷新网页
        time.sleep(5)
        search = self.driver.find_element_by_css_selector("input.but1")  # 重新定位搜索框
        # 滚动滚动条
        self.driver.execute_script("window.scrollBy(0, 800)")
        search_text = self.driver.find_element_by_xpath('//div[@class="gbox"][1]/div/div/a')
        # 断言
        self.assertEqual("衬衫", search.get_attribute("value"))
        self.assertIn("衬衫", search_text.text)

    def testShouye01_07(self):
        '''验证热搜文案显示是否正常'''
        # 定位控件
        qdp = self.driver.find_element_by_css_selector('div.schhot>a:nth-child(1)')
        jzj = self.driver.find_element_by_css_selector('div.schhot>a:nth-child(2)')
        nz = self.driver.find_element_by_css_selector('div.schhot>a:nth-child(3)')
        qcyy = self.driver.find_element_by_css_selector('div.schhot>a:nth-child(4)')
        tsn = self.driver.find_element_by_css_selector('div.schhot>a:nth-child(5)')
        ydnx = self.driver.find_element_by_css_selector('div.schhot>a:nth-child(6)')

        # 断言
        self.assertEqual("9.9抢大牌", qdp.text)
        self.assertEqual("家装节", jzj.text)
        self.assertEqual("男装", nz.text)
        self.assertEqual("全场一员", qcyy.text)
        self.assertEqual("T恤男2016", tsn.text)
        self.assertEqual("运动男鞋", ydnx.text)

    def testShouye01_08(self):
        '''验证点击热搜文案是否能自动填入搜索框，并且搜索正确结果'''
        # 定位并点击“家装节”
        self.driver.find_element_by_css_selector("div.schhot>a:nth-child(2)").click()
        time.sleep(2)
        # 获取搜索框的value属性值
        self.driver.refresh()
        time.sleep(3)
        value = self.driver.find_element_by_name("key").get_attribute("value")
        # 获取搜索结果
        result = self.driver.find_element_by_css_selector("div.nomsg")
        # 断言
        self.assertEqual("家装节", value)
        self.assertEqual("抱歉，没有找到相关的商品", result.text)

    def testShouye01_09(self):
        '''验证非首页页面下精选商品分类文字的悬停显示菜单功能是否正常'''
        # 进入家装节搜索页面
        self.driver.find_element_by_css_selector("div.schhot>a:nth-child(2)").click()
        time.sleep(2)
        # 鼠标挪到“精选商品分类”上
        MoveTo(self.driver).moveto("css", "span.name>em:nth-child(2)")
        time.sleep(3)
        # 获取菜单控件的文本信息
        nn = self.driver.find_element_by_xpath("//dl[@class='type'][1]/dt/div/span/a").text
        xb = self.driver.find_element_by_css_selector("dl.type:nth-child(2)>dt>div>span>a").text
        jd = self.driver.find_element_by_xpath("//dl[@class='type'][3]/dt/div/span/a").text
        zb = self.driver.find_element_by_xpath("//dl[@class='type'][4]/dt/div/span/a").text
        jf = self.driver.find_element_by_xpath("//dl[@class='type'][5]/dt/div/span/a").text
        ms = self.driver.find_element_by_xpath("//dl[@class='type'][6]/dt/div/span/a").text
        my = self.driver.find_element_by_xpath("//dl[@class='type'][7]/dt/div/span/a").text
        yd = self.driver.find_element_by_xpath("//dl[@class='type'][8]/dt/div/span/a").text
        qc = self.driver.find_element_by_xpath("//dl[@class='type'][9]/dt/div/span/a").text
        wj = self.driver.find_element_by_xpath("//dl[@class='type'][10]/dt/div/span/a").text
        bb = self.driver.find_element_by_xpath("//dl[@class='type'][11]/dt/div/span/a").text

        # 断言
        self.assertEqual("男装女装", nn)
        self.assertEqual("鞋子包包", xb)
        self.assertEqual("家电数码", jd)
        self.assertEqual("美妆珠宝", zb)
        self.assertEqual("家居纺织", jf)
        self.assertEqual("美食特产", ms)
        self.assertEqual("母婴玩具", my)
        self.assertEqual("运动健身", yd)
        self.assertEqual("汽车用品", qc)
        self.assertEqual("五金办公", wj)
        self.assertEqual("包包", bb)

    def testShouye01_10(self):
        '''验证精选商品分类下的一级菜单跳转功能是否正确'''
        # 进入家装节搜索页面
        self.driver.find_element_by_css_selector("div.schhot>a:nth-child(2)").click()
        time.sleep(2)
        # 鼠标挪到“精选商品分类”上
        MoveTo(self.driver).moveto("css", "span.name>em:nth-child(2)")
        time.sleep(3)
        # 定位并点击“男装女装”
        self.driver.find_element_by_css_selector("dl.type:nth-child(1)>dt>div>span>a").click()
        # 页面跳转
        path_text = self.driver.find_element_by_css_selector("div.dh").text

        self.assertIn("您当前的位置：网站首页 >> 男装女装", path_text)

    def testShouye01_11(self):
        '''验证秒杀功能是否有效'''
        # 调用pagenew模块新页面方法
        NewPage(self.driver).c_newpage("div.nav_pub>a:nth-child(2)")
        # 获取跳转后页面信息
        xs_text = self.driver.find_element_by_css_selector('div.bnma>a:nth-child(1)').text
        jj_text = self.driver.find_element_by_css_selector('div.bnma>a:nth-child(2)').text
        # 断言
        self.assertEqual("限时抢购", xs_text)
        self.assertEqual("即将开始", jj_text)

    def testShouye01_12(self):
        '''验证商品链接能否正常跳转商品详情页'''
        # 搜索 女装
        self.driver.find_element_by_css_selector("input.but1").send_keys("女装")
        self.driver.find_element_by_css_selector("input.but2").click()
        time.sleep(2)
        # 获取第一条搜索结果的title
        aa = self.driver.find_element_by_xpath("//div[@class='goodsbox']/div[1]/div[3]/div/a").text
        # 点击第一条搜索结果，调用新页面方法
        NewPage(self.driver).p_newpage("//div[@class='goodsbox']/div[1]/div[3]/div/a")
        # 定位商品详情页的商品名
        good_name = self.driver.find_element_by_css_selector("div.info>h1:nth-child(1)")

        # 断言
        self.assertEqual(aa, good_name.text)

if __name__ == "__main__":
    unittest.main()
