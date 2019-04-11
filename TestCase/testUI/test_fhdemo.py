from Common.baseui import baseUI
from Common.Assert import Assertions
import time

class TestFirstUIDemo:
    def test_demo(self, driver):
        base = baseUI(driver)
        driver.get("http://192.168.60.132/#/login")
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')]")
        # 点击订单
        base.click("点击订单","//span[text()='订单']")
        # 点击订单列表
        base.click("点击订单列表","//span[text()='订单列表']")
        # 点击订单状态
        base.click("点击订单状态","//label[contains(text(),'订单状态')]/following-sibling::div//input")
        # 点击待发货
        base.click("点击待发货","//span[text()='待发货']")
        # 点击查询搜索
        base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
        # 记录订单编号
        num = base.get_text("记录编号", "//te[2]//td[2]//div")
        order_num=base.get_text("记录订单编号","//tr[2]//td[3]//div")
        # 点击订单发货
        base.click("点击订单发货", "//span[text()='订单发货']")
        # 点击配送方式
        base.click("点击配送方式", "//input[@placeholder='请选择物流公司']")
        # 点击顺丰快递
        base.click("点击顺丰快递","//span[text()='顺丰快递']")
        # 输入物流单号
        base.send_keys("输入物流单号","//tbody//td[7]//input","123456")
        # 点击确定
        base.click("点击确定","//span[text()='确定']")
        # 点击确定
        base.click("点击确定", "(//span[contains(text(),'确定')])[2]")
        # print(driver.page_source)
        # 断言
        by_xpath = driver.find_element_by_xpath("//div[contains(@role,'alert')]/p")
        assertions = Assertions()
        assertions.assert_in_text(by_xpath.text, '发货成功')
        # 输入搜索
        base.send_keys("输入搜索", "//label[contains(text(),'输入搜索')]/following-sibling::div//input", order_num)
        # 点击查询搜索
        base.click("点击查询搜索", "//span[contains(text(),'查询搜索')]")
        # 定位到刚才发货的订单
        nums = driver.find_element_by_xpath("(//tbdoy)[1]/tr/td[2]")
        # 存放瑟吉欧鸡皮自己安排到编号 找到true 未找到false
        b = False
        # 遍历上边的list
        for n in nums:
            # n.text取出文件的可是文本
            print(n.text)
            # 判断可是文本时候与发货订单编号相同
            if n.text ==num:
                # 如果相同。就将true赋值给B
                b = True
        # 断言，订单状态转换时候正确
        assert True == b
        time.sleep(3)