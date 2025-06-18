from bs4 import BeautifulSoup
import requests

# YC Hack scraping ----------------------
yc_response = requests.get("https://news.ycombinator.com/news")
yc_response.raise_for_status()
yc_page = yc_response.text

soup = BeautifulSoup(yc_page, "html.parser")

article_tag = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article in article_tag:
    article_texts.append(article.getText())
    article_links.append(article.find(name="a").get("href"))
article_upvotes = [int(score.string.split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)

most_ups = max(article_upvotes)
print(most_ups)
most_ups_idx = article_upvotes.index(most_ups)
print(article_texts[most_ups_idx])
print(article_links[most_ups_idx])

# bs4 review ----------------------

# # import lxml # other parsing format

# with open("website.html") as website:
#     contents = website.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.a)
# # print(soup.li)

# anchor_tags = soup.find_all(name="a")
# # for tag in anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)

# name = soup.select_one(selector="#name")
# # print(name)

# headings = soup.select(".heading")
# print(headings)