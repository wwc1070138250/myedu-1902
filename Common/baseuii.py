from selenium import webdriver
from Common.Assert import Assertions
import time
import os


def send_keys(driver,xpath,text):
    username = driver.find_element_by_xpath(xpath)
    username.clear()
    username.send_keys(text)
    time.sleep(2)