import re
import os
import pandas as pd
import requests
from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime

try:
    os.mkdir("data")
except:
    pass

date = datetime.now().strftime("%Y%m%d")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

station_dic = {
    "中野":"A1319/A131902/R7049",
    "高円寺":"A1319/A131904/R3782",
    "阿佐ヶ谷":"A1319/A131905/R205",
    "荻窪":"A1319/A131906/R1973",
    "西荻窪":"A1319/A131907/R7361",
    "吉祥寺":"A1320/A132001/R3232",
    "三鷹":"A1320/A132002/R9481"
    }

pattern = re.compile(r'.+?駅.+?m /')

for station_name, station_id in station_dic.items():

    cnt = 1
    li = []

    while True:

        sleep(1)

        url = "https://tabelog.com/tokyo/{}/rstLst/{}/?svd={}&svt=1900&svps=2".format(station_id, cnt, date)
        html = requests.get(url, headers=headers)

        if html.status_code != 200:
            break

        soup = BeautifulSoup(html.content, "lxml")
        li += [re.sub(pattern, '', str(i)).replace('</span>', '') for i in soup.find_all("span", class_="list-rst__area-genre cpy-area-genre")]

        cnt += 1

    se = pd.Series(li)
    se.to_csv("data/" + station_name + "_" + ".csv", index=False)
