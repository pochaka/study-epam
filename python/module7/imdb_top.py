import requests
import bs4
from re import match, compile, search, sub
import json

class Movie:
    def __init__(self, position, title, year, director, crew, rating):
        self.position = position
        self.title = title
        self.year = year
        self.director = director
        self.crew = crew
        self.rating = rating

    def __repr__(self):
        return f"Movie({self.title}, {self.year}, {self.position}, {self.rating}, {self.director}, {self.crew})"

    def __str__(self):
        return f"{self.title}, {self.year}"

    @property
    def position(self):
        return f"{self.position}"
    
    @position.setter
    def position(self, position):
        self.position = position

    @property
    def title(self):
        return f"{self.title}"

    @title.setter
    def title(self, title):
        self.title = title

    @property
    def year(self):
        return f"{self.year}"
    
    @year.setter
    def year(self, year):
        self.year = year

    @property
    def director(self):
        return f"{self.director}"
    
    @director.setter
    def director(self, director):
        self.director = director

    @property
    def crew(self):
        return f"{self.crew}"

    @crew.setter
    def crew(self, crew):
        self.crew = crew

    @property
    def rating(self):
        return f"{self.rating}"

    @rating.setter
    def rating(self, rating):
        self.rating = rating

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