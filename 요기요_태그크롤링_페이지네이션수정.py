from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
import os
import driver as driver
import requests
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv

driver = wd.Chrome('../webdriver/chromedriver.exe')

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

time.sleep(3) #웹 페이지 로드를 보장하기 위해 3초 쉬기

#

id = 'gg__heon'
password = 'Derek2020@'
id_input = driver.find_elements_by_css_selector('#react-root > section > main > div > article > div > div > div > form > div > div > label > input')[0]
id_input.send_keys(id)
password_input = driver.find_elements_by_css_selector('#react-root > section > main > div > article > div > div > div > form > div > div > label > input')[1]
password_input.send_keys(password)
password_input.submit()

time.sleep(5)

#

driver.get('https://www.instagram.com/explore/tags/배달의민족')

time.sleep(5)

instagram_tags = []
instagram_tag_dates = []

#driver = wd.Chrome("../webdriver/chromedriver.exe")
#driver.get(url)
time.sleep(5)
#태그 디렉 크롤링

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()

for i in range(2000):
    time.sleep(1)
    try:
        data = driver.find_element_by_css_selector('.C7I1f.X7jCj') # C7I1f X7jCj
        tag_raw = data.text
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
        tag = ''.join(tags).replace("#"," ") # "#" 제거

        tag_data = tag.split()

        for tag_one in tag_data:
            instagram_tags.append(tag_one)
            print(instagram_tags)

        date = driver.find_element_by_css_selector("time.FH9sR.Nzb55").text # 날짜 선택

        if date.find('시간') != -1 or date.find('일') != -1 or date.find('분') != -1:
            instagram_tag_dates.append('0주')
        else:
            instagram_tag_dates.append(date)
        print(instagram_tag_dates)
    except:
        instagram_tags.append("error")
        instagram_tag_dates.append('error')
    try:
        print('--count :', i)
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a._65Bje.coreSpriteRightPaginationArrow')))
        driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
        print(len(instagram_tags))
    except:

        f = open('배달의민족_키워드_크롤링.txt', 'w', encoding='utf-8', newline='')
        z = open('배달의민족_키워드_주별언급.txt', 'w', encoding='utf-8', newline='')

        # 크롤링 태그 키워드 저장
        for x in instagram_tags:
            tags = x
            f.write(str(tags) + '\n')
        f.close()
        # 크롤링 날짜 저장
        for o in instagram_tag_dates:
            dates = o
            z.write(str(dates) + '\n')
        z.close()
        driver.close()
    # date = datum2.text
    # #print(date)
    time.sleep(3)

print('----마지막전---')
print(instagram_tag_dates)
print(instagram_tags)

f = open('배달의민족_키워드_크롤링.txt', 'w', encoding='utf-8', newline='')
z = open('배달의민족_키워드_주별언급.txt', 'w', encoding='utf-8', newline='')

#크롤링 태그 키워드 저장
for x in instagram_tags:
    tags = x
    f.write(str(tags) + '\n')
f.close()
#크롤링 날짜 저장
for o in instagram_tag_dates:
    dates = o
    z.write(str(dates) + '\n')
z.close()
driver.close()
# csvWriter = csv.writer(f)
# for i in instagram_tags:
#     csvWriter.writerow(i)
# for z in instagram_tag_dates:
#     csvWriter.writerow(z)
# f.close()
# z.close()
