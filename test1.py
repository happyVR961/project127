import requests 
from bs4 import BeautifulSoup
import csv
startUrl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(startUrl)
# print(page)
soup = BeautifulSoup(page.text, "html.parser")
# def scrapedata():
table1 = soup.find("table")
# print(table1)
tablerow = table1.find_all("tr")
# print(tablerow)
stars_data = []
headers = ["Name", "Distance", "Mass", "Radius"]
name = []
distance = []
mass = []
radius = []
for table in tablerow:
    td = table.find_all("td")
    # td1 = td.find("a")
    stars_data.append(td)
print(stars_data)
for i in range(1, len(stars_data)):
    name.append(stars_data[i][1])
    distance.append(stars_data[i][3])
    mass.append(stars_data[i][5])
    radius.append(stars_data[i][6])
print(name)
print(distance)
print(mass)
print(radius)
with open("happy.csv", "w", encoding = "utf-8") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(name)
    csvWriter.writerows(distance)
    csvWriter.writerows(mass)
    csvWriter.writerows(radius)

