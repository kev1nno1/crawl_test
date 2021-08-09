import requests
from bs4 import BeautifulSoup
import datetime

from newspaper import Article
import json
from newspaper import build

#cannot read vietnamese
#date and time seeems weird
#

#This function returns all the url found in base url given ie
# 'https://vnexpress.net', 'https://cnn.com...
def get_articles_url(url):
    url_set = []
    setset = set()
    articles = build(url, memoize_articles=False)

    for article in articles.articles:
        if article.url not in setset:
            setset.add(article.url)
            url_set.append(article.url)
    return url_set


#This function  return date, content, and article's title
# and return in json format
def date_and_content(url):

    data = []
    article = Article(url )
    article.download()
    article.parse()
    content = article.text
    date = article.publish_date
    title = article.title

    if date is not None:
        date = date.strftime('%Y-%m-%d')
        data.append({
            "Title": title,
            "date":date,
            "Content": content,
        })
    else:
        data.append({
            "Title": title,
            "date": "no date found",
            "Content": content,
        })
    data2 = json.dumps(data)
    return data2

# Same as the function above but trying to make it read vietnamese news
def date_and_content_vi(url):
    data = []
    article = Article(url, language='vi')
    article.download()
    article.parse()
    content = article.text
    date = article.publish_date
    title = article.title

    if date is not None:
        date = date.strftime('%Y-%m-%d')
        data.append({
            "Title": title,
            "date":date,
            "Content": content,
        })
    else:
        data.append({
            "Title": title,
            "date": "no date found",
            "Content": content,
        })
    data2 = json.dumps(data)
    return data2


# TESTING SECTION


#origin_url = 'https://vnexpress.net'
origin_url = 'https://cnn.com'
url_set = get_articles_url(origin_url)

for url in url_set:
    #print(url)
    dt = date_and_content(url)
    print(dt)


# beautifulsoup example

#number= ["1","2","3","4","5"]
# for i in range(5):
#     url = "https://www.bbc.co.uk/search?q=crypto+currency&page="
#
#     new_link = url + number[i]
#     print(new_link)
#     response = requests.get(new_link)
#     soup = BeautifulSoup(response.content, "html.parser")
#     articles = soup.find_all('div', class_='ssrcss-1cbga70-Stack e1y4nx260')
#
#
#     for article in articles:
#         title = article.find('span',{"aria-hidden":"false"})
#
#         link = article.find('a').attrs["href"]
#         print('\n')
#         print(title.get_text())
#         print (link)
#         print ("--------------------")



