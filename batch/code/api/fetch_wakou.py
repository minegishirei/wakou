import requests
from bs4 import BeautifulSoup
import time

def fetch_event_list(year=2023, month=8, day=21):
    url = f"""https://www.city.wako.lg.jp/home/kensaku/event.html?wyear13259={year}&wmonth13259={month}&wday13259={day}"""
    time.sleep(1)
    r = requests.get(url)
    bsObj = BeautifulSoup(r.text, 'html.parser')
    for weekCalendarTr in bsObj.find_all("tr", attrs={ 'class': "weekCalendarTr" }):
        td_list = weekCalendarTr.find_all("td")
        yield {
            "date" : td_list[0].text,
            "link" : td_list[1].find("a").get("href") if td_list[1].find("a") else None,
            "title": td_list[1].find("a").text if td_list[1].find("a") else None,
        }

#https://www.city.wako.lg.jp/home/kyoiku/rekisi/gyo_bunka_1_2/_16836/sunazalea_event/_22301.html


def fetch_event_details(link):
    url = f"""https://www.city.wako.lg.jp{link}"""
    time.sleep(1)
    r = requests.get(url)
    bsObj = BeautifulSoup(r.text, 'html.parser')
    event_details = {}
    for weekCalendarTr in bsObj.find_all("tr"):
        td_list = weekCalendarTr.find_all("td")
        if len(td_list) > 1 and key_clear(td_list[0].getText()):
            event_details.update({
                key_clear(td_list[0].getText()) : value_celar(td_list[1].getText())
            })
    return event_details



def key_clear(origin):
    router = {
        "日付" : "date",
        "開演" : "open_at",
        "場所" : "location",
        "入場方法" : "fee",
        "主催 ・ 後援" : "powerd_by",
        "詳細" : "detail_link",
        "問い合わせ" : "ask"
    }
    for key, value in router.items():
        if key in origin:
            return value

def value_celar(origin):
    router = {
        "\xa0" : " ",
        "\u3000" : " ",
        "\n" : ""
    }
    for key, value in router.items():
        origin = origin.replace(key, value)
    return origin







