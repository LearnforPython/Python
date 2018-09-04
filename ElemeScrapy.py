from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver
import json


headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

chromedriverpath = r"C:\Users\kmao009\Documents\chromedriver.exe"

mainUrl = "https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3985r58m2&latitude={}&longitude={}&terminal=web&offset=0&limit=25"

menuUrl = "https://www.ele.me/restapi/shopping/v2/menu?restaurant_id={}&terminal=web"

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

def getAllrestaurantByGeo(latitude,longitude,headers):
    url = mainUrl.format(latitude,longitude)
    restaurants_html = simple_get(url,headers)
    restaurants_array = json.loads(restaurants_html.text)
    restaurantIds = []
    for restaurant in restaurants_array:
        print(restaurant['id'])
        # restaurant_details = restaurant['folding_restaurants']
        # for detail in restaurant_details:
        #     print(detail['name'])
        restaurantIds.append(restaurant['id'])
    return restaurantIds



# raw_html = simple_get('https://www.ele.me/restapi/shopping/v2/menu?restaurant_id=165991466&terminal=web',headers)

# json_array = json.loads(raw_html.text)


# for info in json_array:
#     foodarray = info['foods']
#     for foodinfo in foodarray:
#         specfoods = foodinfo['specfoods']
#         for specfood in specfoods:
#             fooddetail = str(specfood['name']) + " : " + str(specfood['price']) + ", " + str(specfood['specs'])
#             print(fooddetail)

def listAllMenuByrestaurant(latitude,longitude,headers):
    ids = getAllrestaurantByGeo(latitude,longitude,headers)
    for id in ids:
        tmpUrl = menuUrl.format(id)
        menuhtml = simple_get(tmpUrl,headers)
        menu_array = json.loads(menuhtml.text)
        for info in menu_array:
            foodarray = info['foods']
            for foodinfo in foodarray:
                specfoods = foodinfo['specfoods']
                for specfood in specfoods:
                    fooddetail = str(specfood['name']) + " : " + str(specfood['price']) + ", " + str(specfood['specs'])
                    print(fooddetail)


listAllMenuByrestaurant('31.202375','121.359601',headers)

