from Common.baseui import baseUI
from Common.Assert import Assertions

class TestFirstUIDemo:
    def test_demo(self, driver):
        base = baseUI(driver)
        driver.get("http://192.168.60.132/#/login")
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录
        base.click("点击登录", "//span[contains(text(),'登录')]")
        # 点击营销
        base.click("点击营销","//span[text()='营销']")
        # 点击优惠券列表
        base.click("点击优惠券列表","//span[text()='优惠券列表']")
        # 点击编辑
        base.click("点击编辑","//span[contains(text(),'编辑')]")
        # 修改使用门槛
        base.send_keys("修改使用门槛","//label[contains(text(),'使用门槛：')]/following-sibling::div//input","300")
        # 点击提交
        base.click("点击提交","//span[text()='提交']")
        # 点击确定
        base.click("点击确定","//span[contains(text(),'确定')]")
        print(driver.page_source)
        # 添加断言
        xpath = driver.find_element_by_xpath("//div[contains(@role,'alert')]/p")
        # print(xpath.text)
        assertions = Assertions()
        assertions.assert_in_text(xpath.text,'修改成功')
