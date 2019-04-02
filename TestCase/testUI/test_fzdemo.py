from selenium import webdriver
from Common.Assert import Assertions
import time
import os
from Common.baseui import baseUI
from Common import baseui
# from Common.baseuii import *

class TestFirstUIDemo:
    def test_demo(self,driver):
        base = baseUI(driver)
        # 打开网页
        driver.get("http://192.168.60.132/#/login")
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录
        base.click("点击登录","//span[contains(text(),'登录')]")
        # 点击商品
        base.click("点击商品","(//span[contains(text(),'商品')])[1]")
        # 填写添加商品
        base.click("点击添加商品","(//span[contains(text(),'添加商品')])[1]")
        # 点击商品分类
        base.click("点击商品分类","(//label[contains(text(),'商品分类：')]/following-sibling::div//span)[4]")
        # 点击手机数码
        base.click("点击手机数码","//li[contains(text(),'手机数码')]")
        # 点击手机通讯
        base.click("点击手机通讯","//li[contains(text(),'手机通讯')]")
        # 输入商品名称
        base.send_keys("输入商品名称","//label[contains(text(), '商品名称：')]/following-sibling::div//input","三星")
        # 输入副标题
        base.send_keys("输入副标题","//label[contains(text(),'副标题：')]/following-sibling::div//input","XXX")
        # 点击商品品牌
        base.click("点击商品品牌","//label[contains(text(),'商品品牌：')]/following-sibling::div//input")
        # 点击三星
        base.click("点击三星","//span[contains(text(),'三星')]")
        # 商品介绍
        base.send_keys("填写商品介绍","//label[contains(text(),'商品介绍：')]/following-sibling::div//textarea","XXX")
        # 商品货号
        base.send_keys("填写商品货号","//label[contains(text(),'商品货号：')]/following-sibling::div//input","XXX")
        # 商品售价
        base.send_keys("填写商品售价","//label[contains(text(),'商品售价：')]/following-sibling::div//input","1000")
        # 市场价
        base.send_keys("填写市场价","//label[contains(text(),'市场价：')]/following-sibling::div//input","1001")
        # 商品库存
        base.send_keys("填写商品库存","//label[contains(text(),'商品库存：')]/following-sibling::div//input","11")
        # 计量单位
        base.send_keys("填写计量单位","//label[contains(text(),'计量单位：')]/following-sibling::div//input","个")
        # 商品重量
        base.send_keys("填写商品重量","//label[contains(text(),'商品重量：')]/following-sibling::div//input","8")
        # 排序
        base.send_keys("填写排序","//label[contains(text(),'排序')]/following-sibling::div//input","1")
        # 点击下一步
        base.click("点击下一步","//span[contains(text(),'下一步，填写商品促销')]")
        # 点击预告商品
        base.click("点击预告商品","//label[contains(text(),'预告商品：')]/following-sibling::div//span")
        # 点击商品上架
        base.click("点击商品上架","//label[contains(text(),'商品上架：')]/following-sibling::div//span")
        # 点击商品推荐
        base.click("点击商品推荐","(//label[contains(text(),'商品推荐：')]/following-sibling::div//span)[4]")
        # 点击服务保证
        base.click("点击服务保证","(//label[contains(text(),'服务保证：')]/following-sibling::div//span)[1]")
        # 点击特惠促销
        base.click("点击特惠促销","//span[contains(text(),'特惠促销')]")
        # 开始时间
        base.send_keys("填写开始时间","//div[contains(text(),'开始时间')]//following-sibling::div//input","2019-04-03 00:00:00")
        # 结束时间
        base.send_keys("填写结束时间","//div[contains(text(),'结束时间')]//following-sibling::div//input","2019-04-13 00:00:00")
        # 促销价格
        base.send_keys("填写促销价格","//div[contains(text(),'促销价格')]//following-sibling::div//input","998")
        # 下一步
        base.click("点击下一步","//span[contains(text(),'下一步，填写商品属性')]")

        base.click("点击下一步","//span[contains(text(),'下一步，选择商品关联')]")

        base.click("点击下一步","//span[contains(text(),'完成，提交商品')]")
