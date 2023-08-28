import requests
from bs4 import BeautifulSoup
import time



url = "https://www.wakolib.jp"

def fetch_lib_event_list():
    print(url)
    r = requests.get(url + "/eventnews/")
    bsObj = BeautifulSoup(r.content, 'html.parser')
    eventBsObj = bsObj.find("div", {"id" : "link_contents_news"} )
    event_list = []
    for li in  eventBsObj.find_all("li"):
        event_list.append({
            "date" : li.find("span", { "class":"update_date"}).getText(),
            "title" : "和光図書館" + li.find("span", { "class":"news_description"}).getText(),
            "detail_link" : url + li.find("span", { "class":"news_description"}).find("a").get("href")
        })
    return event_list



def fetch_event_details(url):
    r = requests.get(url)
    bsObj = BeautifulSoup(r.content, 'html.parser')
    main_containt = bsObj.find("div", {"class": "content_wrap"})

    event_details = {
        "description": main_containt.getText(),
    }
    if main_containt.find_all("img"):
        event_details.update({"images" : [ url + img.get("src") for img in main_containt.find_all("img")] })
    return event_details

