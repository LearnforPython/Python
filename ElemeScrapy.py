from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver


headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

chromedriverpath = r"C:\Users\kmao009\Documents\chromedriver.exe"

def simple_get(url,headers):

    browser = webdriver.Chrome(chromedriverpath)
    browser.get(url)
    page = BeautifulSoup(browser.page_source,"html.parser")
    return page

def is_good_respoonse(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html')>-1)

def log_error(e):
    print(e)

raw_html = simple_get('https://www.ele.me/place/wtw3985r58m2?latitude=31.202375&longitude=121.359601',headers)
print(raw_html)