import requests
import bs4
from re import match, compile, search, sub
import json

url = "https://imdb.com/chart/top"

page = requests.get(url, headers = {"Accept-Language": "en-US"})
if page.status_code == 200:
    print("Page is OK. Processing...")
else:
    print("Page is not available.")
    exit()

movies = []
positions = []
titles = []
years = []
directors = []
crews = []
ratings = []

dir_regex = compile(r".+(?=\s\(dir\.\))")
crew_regex = compile(r"(?<=\(dir\.\),\s).+")
pos_regex = compile(r"([0-9]{1,3})(?=\.)")

soup = bs4.BeautifulSoup(page.text, "html.parser")

for item in soup.find_all('td', class_ = "ratingColumn imdbRating"):
    ratings.append(float(item.text.replace("\n", "")))

for item in soup.find_all('td', class_ = "titleColumn"):
    direc = match(dir_regex, item.findChild('a')['title'])
    crew = search(crew_regex, item.findChild('a')['title'])
    directors.append(direc[0])
    crews.append(crew[0])
    titles.append(item.findChild('a').text)
    years.append(int(sub(r'\(|\)', '', item.findChild('span').text)))
    pos = search(pos_regex, item.text)
    positions.append(int(pos[0]))

for i in range(len(positions)):
    a = {titles[i]:{"Position": positions[i], "Year": years[i], "Director": directors[i], "Crew": crews[i], "Rating": ratings[i]}}
    movies.append(a)

with open("data.json", 'w') as jsn:
    json.dump(movies, jsn, ensure_ascii=False, indent=4)