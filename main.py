from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = ("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
stars = requests.get(START_URL)
soup = BeautifulSoup(stars.text, "html.parser")
star_lists = []
for star_data in soup.find("table").find_all("tr"):
    table_headings = star_data.find_all("th")
    list = [i.text.rstrip() for i in table_headings]
    star_lists.append(list)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(star_lists)):
    name.append(star_lists[i][1])
    distance.append(star_lists[i][3])
    mass.append(star_lists[i][5])
    radius.append(star_lists[i][6])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")
