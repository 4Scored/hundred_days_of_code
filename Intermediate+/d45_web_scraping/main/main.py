import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
top_movies_response = requests.get(URL)
top_movies_response.raise_for_status()
top_movies_html = top_movies_response.text

soup = BeautifulSoup(top_movies_html, "html.parser")

movie_tags = soup.find_all(name="h2") # extract h2s, then strong below
movie_names = [tag.get_text(strip=True) for tag in movie_tags if tag.find("strong")] # <strong> is a nested tag

movie_names = movie_names[::-1]    
print(movie_names)

with open("movies.txt", mode="w") as file:
    for movie in movie_names:
        file.write(f"{movie}\n") 