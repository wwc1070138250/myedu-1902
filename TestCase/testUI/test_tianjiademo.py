from selenium import webdriver
from Common.Assert import Assertions
import time
import os
from Common.baseui import baseUI
# from Common.baseuii import *

class TestFirstUIDemo:
    def test_demo(self,driver):
        base = baseUI(driver)
        # 打开网页
        driver.get("http://192.168.60.132/#/login")
        base.send_keys("输入用户名","//input[@name='username']","admin")
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # send_keys(driver,"//input[@name='username']","admin")
        # send_keys(driver,"//input[@name='password']","123456")
        # 输入用户名
        # username = driver.find_element_by_xpath("//input[@name='username']")
        # username.clear()
        # username.send_keys("admin")
        # time.sleep(2)
        # 输入密码
        # password = driver.find_element_by_xpath("//input[@name='password']")
        # password.clear()
        # password.send_keys("123456")
        # time.sleep(2)
        # 点击登录
        login = driver.find_element_by_xpath("//span[contains(text(),'登录')]")
        login.click()
        time.sleep(1)
        # 点击商品
        login = driver.find_element_by_xpath("(//span[contains(text(),'商品')])[1]")
        login.click()
        time.sleep(1)
        # 点击添加商品
        login = driver.find_element_by_xpath("(//span[contains(text(),'添加商品')])[1]")
        login.click()
        time.sleep(1)
        # 点击商品分类
        login = driver.find_element_by_xpath("(//label[contains(text(),'商品分类：')]/following-sibling::div//span)[4]")
        login.click()
        time.sleep(1)
        # 点击手机数码
        login = driver.find_element_by_xpath("//li[contains(text(),'手机数码')]")
        login.click()
        time.sleep(1)
        # 点击手机通讯
        login = driver.find_element_by_xpath("//li[contains(text(),'手机通讯')]")
        login.click()
        time.sleep(1)
        # 输入商品名称
        username = driver.find_element_by_xpath("//label[contains(text(), '商品名称：')]/following-sibling::div//input")
        username.clear()
        username.send_keys("三星")
        time.sleep(1)
        # 输入副标题
        username = driver.find_element_by_xpath("//label[contains(text(),'副标题：')]/following-sibling::div//input")
        username.clear()
        username.send_keys("XXX")
        time.sleep(1)
        # 点击商品品牌
        login = driver.find_element_by_xpath("//label[contains(text(),'商品品牌：')]/following-sibling::div//input")
        login.click()
        time.sleep(1)
        # 点击三星
        login = driver.find_element_by_xpath("//span[contains(text(),'三星')]")
        login.click()
        time.sleep(1)
        # 商品介绍
        username = driver.find_element_by_xpath("//label[contains(text(),'商品介绍：')]/following-sibling::div//textarea")
        username.clear()
        username.send_keys("XXX")
        time.sleep(1)
        # 商品货号
        username = driver.find_element_by_xpath("//label[contains(text(),'商品货号：')]/following-sibling::div//input")
        username.clear()
        username.send_keys("XXX")
        time.sleep(1)
        # 商品售价
        username = driver.find_element_by_xpath("//label[contains(text(),'商品售价：')]/following-sibling::div//input")
        username.clear()
        username.send_keys("1000")
        # time.sleep(1)
        # 市场价
        username = driver.find_element_by_xpath("//label[contains(text(),'市场价：')]/following-sibling::div//input")
        username.clear()
        username.send_keys("1001")
        # time.sleep(1)
        # 商品库存
        username = driver.find_element_by_xpath("//label[contains(text(),'商品库存：')]/following-sibling::div//input")
        username.clear()
        username.send_keys("11")
        # time.sleep(1)
        # 计量单位
        username = driver.find_element_by_xpath("//label[contains(text(),'计量单位：')]/following-sibling::div//input")
        username.clear()
        username.send_keys("2")
        # time.sleep(1)
        # 商品重量
        username = driver.find_element_by_xpath("//label[contains(text(),'商品重量：')]/following-sibling::div//input")
        username.clear()
        username.send_keys("8")
        # time.sleep(1)
        # 排序
        username = driver.find_element_by_xpath("//label[contains(text(),'排序')]/following-sibling::div//input")
        username.clear()
        username.send_keys("1")
        # time.sleep(1)
        # 点击下一步
        login = driver.find_element_by_xpath("//span[contains(text(),'下一步，填写商品促销')]")
        login.click()
        # time.sleep(1)
        # 点击预告商品
        login = driver.find_element_by_xpath("//label[contains(text(),'预告商品：')]/following-sibling::div//span")
        login.click()
        # time.sleep(1)
        # 点击商品上架
        login = driver.find_element_by_xpath("//label[contains(text(),'商品上架：')]/following-sibling::div//span")
        login.click()
        # time.sleep(1)
        # 点击商品推荐
        login = driver.find_element_by_xpath("(//label[contains(text(),'商品推荐：')]/following-sibling::div//span)[4]")
        login.click()
        time.sleep(1)
        # 点击服务保证
        login = driver.find_element_by_xpath("(//label[contains(text(),'服务保证：')]/following-sibling::div//span)[1]")
        login.click()
        time.sleep(1)
        # 点击特惠促销
        login = driver.find_element_by_xpath("//span[contains(text(),'特惠促销')]")
        login.click()
        time.sleep(1)
        # 开始时间
        username = driver.find_element_by_xpath("//div[contains(text(),'开始时间')]//following-sibling::div//input")
        username.clear()
        username.send_keys("2019-04-03 00:00:00")
        time.sleep(1)
        # 结束时间
        username = driver.find_element_by_xpath("//div[contains(text(),'结束时间')]//following-sibling::div//input")
        username.clear()
        username.send_keys("2019-04-13 00:00:00")
        time.sleep(1)
        # 促销价格
        username = driver.find_element_by_xpath("//div[contains(text(),'促销价格')]//following-sibling::div//input")
        username.clear()
        username.send_keys("998")
        time.sleep(1)
        # 下一步
        login = driver.find_element_by_xpath("//span[contains(text(),'下一步，填写商品属性')]")
        login.click()
        time.sleep(1)

        login = driver.find_element_by_xpath("//span[contains(text(),'下一步，选择商品关联')]")
        login.click()
        time.sleep(1)

        login = driver.find_element_by_xpath("//span[contains(text(),'完成，提交商品')]")
        login.click()
        time.sleep(1)

        # login = driver.find_element_by_xpath("//span[contains(text(),'确定')]")
        # login.click()
        # time.sleep(1)