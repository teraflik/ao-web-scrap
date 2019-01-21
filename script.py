import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

FILE_NAME = "imdb_top_250.csv"
url = "https://www.imdb.com/chart/top"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
print("Exporting {:s}".format(soup.title.text))


fieldnames = ["S. No.", "Movie", "Year", "Director", "Actors"]
movie_file = open('imdb_top_250.csv', mode='w')
movie_writer = csv.DictWriter(movie_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
movie_writer.writeheader()

i = 1
for link in soup.find_all("td", class_="titleColumn"):
    director, actors = link.a['title'].split(" (dir.), ")
    movie = link.a.text
    year = link.span.text.replace("(", "").replace(")", "")
    #print("{:d}, {:s}, {:s}, {:s}, {:s}".format(i, movie, year, director, actors))
    movie_writer.writerow({"S. No.": i, "Movie": movie, "Year": year, "Director": director, "Actors": actors})
    i = i+1

print("Output saved to \"{:s}\"".format(FILE_NAME))