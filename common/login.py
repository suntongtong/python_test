#-*- coding:utf-8 -*-
# @Time  :2020/12/11 13:34
# Author :sunya
# file   :login.py

from selenium import webdriver
import time
import configparser
from common import get_filepath


class Lgoin():
  config_path = get_filepath.config_path
  cf = configparser.ConfigParser()
  cf.read(config_path, encoding="utf-8-sig")
  user_element = cf.get("login_element", "user")
  password_element = cf.get("login_element", "password")
  btn_element = cf.get("login_element", "btn_login")
  labor_img = cf.get("login_element", "labor_img")
  username = cf.get("environment_config", "username")
  userpwd = cf.get("environment_config", "password")
  url = cf.get("environment_config", "url")
  def lgoin_system(self):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(self.url)
    driver.find_element_by_xpath(self.user_element).send_keys(self.username)
    driver.find_element_by_xpath(self.password_element).send_keys(self.userpwd)
    driver.find_element_by_xpath(self.btn_element).click()
    time.sleep(10)
    driver.find_element_by_xpath(self.labor_img).click()
    time.sleep(10)
    laborCookie= driver.get_cookie(name=".JAVA.LABOR.CLOUD.AUTH")["value"] # 获取当前页面的cookie值
    cloudtCookie=driver.get_cookie(name=".JAVA.CLOUD.AUTH")["value"]
    access_Token=driver.get_cookie(name=".CLOUD_ACCESS_TOKEN")["value"]
    header={
      'Cookie': '.CLOUD_ACCESS_TOKEN={access_Token};.JAVA.LABOR.CLOUD.AUTH={laborCookie};.JAVA.CLOUD.AUTH={cloudtCookie}'.format(laborCookie=laborCookie,cloudtCookie=cloudtCookie,access_Token=access_Token)

    }
    return header



