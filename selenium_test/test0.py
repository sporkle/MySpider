from selenium import webdriver
import time

# dr = webdriver.Chrome()
# time.sleep(2)
#
# dr.get('http://www.baidu.com')
# time.sleep(2)
#
# dr.maximize_window()
# time.sleep(2)
#
# dr.set_window_size(256,256)
# time.sleep(2)
#
# print('Chrome will be close.\n')
# dr.quit()
# print('Chrom closed.')

dr = webdriver.Chrome()
first_url = 'http://www.baidu.com/'
dr.get(first_url)
print ('URL of current page is %s')%(dr.current_url)

secend_url = 'http://www.python.org/'
dr.get(secend_url)
print ('URL of current page is %s')%(dr.current_url)
time.sleep(2)

dr.back()
print ('URL of current page is %s')%(dr.current_url)
time.sleep(2)

dr.forward()
print ('URL of current page is %s')%(dr.current_url)

time.sleep(1)

dr.quit()