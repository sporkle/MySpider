# coding = utf-8
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


if __name__ == '__main__':
    driver = webdriver.Firefox()
    html = driver.get('http://www.ygdy8.net/html/gndy/dyzz/20170907/54947.html')
    print driver.current_url
    print driver.title
    # move_name = driver.find_elements_by_xpath('//*[@id="header"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/ul/table/tbody/tr[2]/td[2]/b/a/text()')
    # print type(move_name)
    # print(move_name[0])

    driver.quit()