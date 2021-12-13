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

def get_url(search_term):
    """Generate an url from the search term"""
    template = "https://shopee.com.my/search?keyword={}"
    search_term = search_term.replace(' ', '+')

    # add term query to url
    url = template.format(search_term)

    # add page query placeholder
    url += '&page={}&sortBy=sales'

    return url


def main(search_term):
    # invoke the webdriver
    driver = webdriver.Chrome(options=chrome_options)
    rows = []
    url = get_url(search_term)


    #탐색 page수 지정 (일단 0,1만)
    for page in range(0, 5):
        driver.get(url.format(page))
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "shopee-search-item-result__item")))
        driver.execute_script("""
        var scroll = document.body.scrollHeight / 10;
        var i = 0;
        function scrollit(i) {
           window.scrollBy({top: scroll, left: 0, behavior: 'smooth'});
           i++;
           if (i < 10) {
            setTimeout(scrollit, 500, i);
            }
        }
        scrollit(i);
        """)
        sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', {'class': 'col-xs-2-4 shopee-search-item-result__item'}):
            #상품명
            name = item.find('div', {'class': '_10Wbs- _5SSWfi UjjMrh'})
            if name is not None:
                name = name.text.strip()
            else:
                name = ''
            #상품 가격(최저)
            price = item.find('div', {'class': 'zp9xm9 xSxKlK _1heB4J'})
            if price is not None:
                price = price.find('span', {'class': '_1d9_77'}).text.strip()
            else:
                price = ''

            #판매량(월)
            sold = item.find('div', {'class':'_2VIlt8'})
            if sold is not None:
                sold = sold.text.strip()
            else:
                sold = ''

            #원가(세일 전)
            original_price = item.find('div', {'class':'zp9xm9 hHV8eX _2hXFTl'})
            if original_price is not None:
                original_price = original_price.text.strip()
            else:
                original_price = ''

            #할인율
            dc_rate = item.find('span', {'class': 'percent'})
            if dc_rate is not None:
                dc_rate = dc_rate.text.strip()
            else:
                dc_rate = ''

            #상품 link
            link = item.find('a')
            if link is not None:
                link = link.get('href')
            else:
                link = ''

            print([name, price, sold, original_price, dc_rate, link])
            rows.append([name, price, sold, original_price, dc_rate, link])
    driver.close()
    return rows


# product = pd.DataFrame(main('ricecooker'))
# product.columns = ['name','price','sold','original_price','discount','link']
# dropindex = product.loc[product['link'] == ''].index
# final_product_list = product.drop(dropindex)

# shopee_my = 'https://shopee.com.my/'
# appendix = []


# for i in final_product_list['link']:
#     try:
#         i = shopee_my + i
#         result = get_product_ratings(i)
#         appendix.append(result)
#         print(appendix)
#     except TimeoutException:
#         print('failed')


