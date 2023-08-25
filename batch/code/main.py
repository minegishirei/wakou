from pprint import pprint 
from api.fetch_wakou import fetch_event_list, fetch_event_details
from mydate.date import get_next_target_date
import datetime

def unique_list(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b


def rotate_fetch_eventlist(next_week_amount):
    eventlist = []
    # 現在の日付を取得する。
    today = datetime.date.today()
    next_date = get_next_target_date(today, '月') + datetime.timedelta(days=28)
    for _ in range(0, next_week_amount):
        eventlist.extend(list(fetch_event_list(
            year=next_date.strftime('%Y'),
            month=next_date.strftime('%m'),
            day=next_date.strftime('%d')
        )))
        next_date = next_date + datetime.timedelta(days=7)
    return eventlist

all_events = []
for event in rotate_fetch_eventlist(2):
    if event["link"]:
        all_events.append(fetch_event_details(event["link"]))

pprint( unique_list( all_events) )
    



