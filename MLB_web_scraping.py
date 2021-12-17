import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime

print("Page request sent")
begin = datetime.now()
url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/1"
html_page = requests.get(url)
end = datetime.now()
print("Request finished: {}".format(end-begin))
soup = BeautifulSoup(html_page.text, "html.parser")
#print(soup.find_all('tr', attrs = {'class': 'oddrow player-10-33039'}))
table_html = soup.find_all('table', attrs={"class": "tablehead"})
print(table_html)

for row in table_html[0]:
    cell = table_html[0].findChildren("tr")
    #print(cell)
