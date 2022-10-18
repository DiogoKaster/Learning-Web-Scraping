import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https:"
                            "//www.empireonline.com/movies/features/best-movies-2/")
web_html = response.text
soup = BeautifulSoup(web_html, "html.parser")
web_titles = [movie.getText() for movie in soup.select(selector=".article-title-description__text .title")]
print(web_titles)
with open(file="top-100-movies.txt", mode="w", encoding="utf-8") as file:
    for movie in reversed(web_titles):
        file.write(f"{movie}\n")
