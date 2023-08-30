from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

contents = BeautifulSoup(response.text, "html.parser")


article_texts = [text.getText() for text in contents.select("span.titleline > a:not(span.sitebit > a)")]
article_links = [text.get("href") for text in contents.select("span.titleline > a:not(span.sitebit > a)")]
article_upvotes = [upvote.getText() for upvote in contents.select("span.score")]

print(len(article_texts))
print(len(article_links))
print(len(article_upvotes))

print(article_upvotes)