import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.rte.ie/weather/16366-cork/")
if(page.status_code == 200):
    print("Connection Successful")
else:
    print("Connection Error")

soup = BeautifulSoup(page.content, 'html.parser')
i = 0
tab = "\t"

days = soup.find_all('span', class_="day-name")
temps = soup.find_all('span', class_="day-temperature")
forcs = soup.find_all('span', class_="forecast-icon")

o = 7
while o < len(days):
    days.pop(o)
    temps.pop(o)

print("Weather")
print("_______________________________")
print('{:<10}{:<10}{:<10}'.format("Day","Temp","Weather"))

while i < len(days):
    print('{:<10}{:<10}{:<10}'.format(days[i].text, temps[i].text, forcs[i].get('title')))
    i += 1

finish = False
while(finish == False):
    print("Press enter to continue")
    input("...")
    finish = True