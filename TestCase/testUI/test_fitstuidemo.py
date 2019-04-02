from selenium import webdriver
from Common.Assert import Assertions
import time
import os



class TestFirstUIDemo:
    def test_demo(self):
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__),"../../chromedriver/chromedriver.exe")
        # 打开浏览器
        print(driver_path)
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.implicitly_wait(8)  # 设置隐式时间等待
        time.sleep(2)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        # 通过xpath定位元素
        username = driver.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys("admin")
        time.sleep(2)
        # 输入密码
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys("123456")
        time.sleep(2)
        # 点击登录
        login = driver.find_element_by_xpath("//span[contains(text(),'登录')]")
        login.click()
        time.sleep(2)
        # 断言
        assertions = Assertions()
        assertions.assert_in_text(driver.page_source,'首页')
        # 点击营销
        yingxiao = driver.find_element_by_xpath("//span[contains(text(),'营销')]")
        yingxiao.click()
        time.sleep(2)
        # 点击优惠券列表
        youhuiquan = driver.find_element_by_xpath("//span[contains(text(),'优惠券列表')]")
        youhuiquan.click()
        time.sleep(2)
        # 输入优惠券名称
        mingcheng = driver.find_element_by_xpath("//label[contains(text(),'优惠券名称：')]/following-sibling::div//input")
        mingcheng.clear()
        mingcheng.send_keys("全品类通用券")
        time.sleep(2)
        # 点击查询搜索
        chaxun = driver.find_element_by_xpath("//span[contains(text(),'查询搜索')]")
        chaxun.click()
        time.sleep(2)
        assertions = Assertions()
        assertions.assert_in_text(driver.page_source, '编号')
        # 退出游览器
        driver.quit()



