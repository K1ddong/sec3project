from os import error
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
from get_product import get_product_ratings
from get_product import get_product_spec
from shopee_crawl import get_url,main


products = pd.read_csv('./main_info.csv')

shopee_my = 'https://shopee.com.my'
appendix = []


# for i in products['link']:
#     try:
#         i = shopee_my + i
#         result = get_product_ratings(i)
#         appendix.append(result)
#         print(len(appendix))
#     except:
#         appendix.append('')
#         pass

for i in products['link']:
    try:
        i = shopee_my + i
        result = get_product_ratings(i)
        appendix.append(result)
        print(len(appendix))
    except:
        appendix.append(['','','','','','','','','',''])
        pass
spec_info = pd.DataFrame(appendix,columns=['star','ratings(amount)','total_sales','favorites','brand','weight','warranty','capacity','stock','power'])
spec_info.to_csv('./spec_info.csv', sep=',',na_rep='NaN', encoding='utf_8_sig')