import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates

def makeDates(dates):
    datesArray = []

    for date in dates:
        year, month, day = date.split('-')

        x = datetime.datetime(int(year),int(month),int(day))
        datesArray.append(x)

    return datesArray



#PELAAJAN URL TUNNUS: 5 ensimmäistä kirjainta sukunimestä + 2 ensimmäistä etunimestä + '01'
p = requests.post
url = "https://www.basketball-reference.com/players/d/davisan02/gamelog/2023"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")
table = soup.find(id="pgl_basic")

pointsPerGame = []
dateGame = []
points = ""
dateOfGame = ""

for item in table.find_all('td'):
    #.append(([int(item.string)]))
    if item['data-stat'] == "date_game":
        dateOfGame = item.string

    if item['data-stat'] == "pts":
        points = int(item.string)
        pointsPerGame.append(points)
        dateGame.append(dateOfGame)



pointsPerGame = np.array(pointsPerGame)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=20))
plt.yticks(np.arange(0,pointsPerGame.max() + 5, 2))
plt.ylim(0,pointsPerGame.max() +5)
plt.axhline(y=np.mean(pointsPerGame), color='r', linestyle="-")
plt.plot(makeDates(dateGame),pointsPerGame, marker='o')

print(datetime.datetime.now())
plt.ylabel("Points")
plt.xlabel("Date")
plt.show()






makeDates(dateGame)