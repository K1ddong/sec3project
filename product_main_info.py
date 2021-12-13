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

product = pd.DataFrame(main('ricecooker'), columns=['product_title','lowest_price','montly_sales','original_price','discount_rate','link'])
dropindex = product.loc[product['link'] == ''].index
final_product_list = product.drop(dropindex)
final_product_list.to_csv('./main_info.csv', sep=',',na_rep='NaN', encoding='utf_8_sig')