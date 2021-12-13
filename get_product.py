from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait # 해당 태그를 기다림
from selenium.common.exceptions import TimeoutException # 태그가 없는 예외 처리
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import pandas as pd
import random

chromedriver = './chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless') 
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument("disable-infobars")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})


def get_product_ratings(link):
    details =[]
    # for product in product_links:
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)
    WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "page-product")))
    #사람인척 쉬는 시간 랜덤 배정
    sleep(random.uniform(2,4))
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    #윗 부분 정보 추출
    header = soup.find('div',{'class':'aca9MM'})
    evaluation = soup.find_all('div',{'class':'flex _3A3c6_'})
    favorite = soup.find('div',{'class':'flex items-center _3nBAy8'})

    #아랫 부분 상품 스펙 추출
    specifications = soup.find_all('div',{'class':'aPKXeO'})

    star = evaluation[0].find('div','OitLRu _1mYa1t').text.strip()
    details.append(star)
    ratings = evaluation[1].find('div','OitLRu').text.strip()
    details.append(ratings)
    total_sold = header.text.strip()
    details.append(total_sold)
    favorite = favorite.find('div','_39mrb_').text.strip()
    details.append(favorite)
    specs = get_product_spec(specifications)

    #브라우저 종료
    browser.close()

    for i in specs:
        for x in i:
            details.append(x)
    return details



    #######

def get_product_spec(specifications):
    specs = []
    for detail in specifications:
        category = detail.find('label').text.strip()
        if category == 'Brand':
            brand = detail.find('a').text.strip()
            break
        else:
            brand = ''

    for detail in specifications:
        category = detail.find('label').text.strip()
        if category == 'Weight':
            weight = detail.find('div').text.strip()
            break
        else:
            weight = ''

    for detail in specifications:
        category = detail.find('label').text.strip()
        if category == 'Warranty Duration':
            warranty_duration = detail.find('div').text.strip()
            break
        else:
            warranty_duration = ''

    # for detail in specifications:
    #     category = detail.find('label').text.strip()
    #     if category == 'Warranty Type':
    #         warranty_type = detail.find('div').text.strip()
    #         break
    #     else:
    #         warranty_type = ''

    for detail in specifications:
        category = detail.find('label').text.strip()
        if category == 'Volume Capacity':
            volume = detail.find('div').text.strip()
            break
        else:
            volume = ''

    # for detail in specifications:
    #     category = detail.find('label').text.strip()
    #     if category == 'Number of People':
    #         people = detail.find('div').text.strip()
    #         break
    #     else:
    #         people = ''

    for detail in specifications:
        category = detail.find('label').text.strip()
        if category == 'Stock':
            stock = detail.find('div').text.strip()
            break
        else:
            stock = ''

    # for detail in specifications:
    #     category = detail.find('label').text.strip()
    #     if category == 'Rice Cooker Type':
    #         cooker_type = detail.find('div').text.strip()
    #         break
    #     else:
    #         cooker_type = ''

    # for detail in specifications:
    #     category = detail.find('label').text.strip()
    #     if category == 'Material':
    #         material = detail.find('div').text.strip()
    #         break
    #     else:
    #         material = ''

    for detail in specifications:
        category = detail.find('label').text.strip()
        if category == 'Power Consumption':
            power = detail.find('div').text.strip()
            break
        else:
            power = ''

    specs.append([brand,weight, warranty_duration, volume, stock, power])
    return specs
