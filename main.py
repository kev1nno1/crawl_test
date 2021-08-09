import requests
from bs4 import BeautifulSoup
import datetime

from newspaper import Article
import json
from newspaper import build

#check if string is not blank
def is_not_blank(s):
    return bool(s and not s.isspace())

#This function returns all the url found in base url given: ie
# 'https://vnexpress.net', 'https://cnn.com...



def get_articles_url(url):
    url_set = []
    set_url = set()
    set_title = set()
    articles = build(url, memoize_articles=False)

    for article in articles.articles:
        if article.url not in set_url and article.title not in set_title:
            set_url.add(article.url)
            set_title.add(article.title)
            url_set.append(article.url)

    return url_set



#This function  return date, content, and article's title
# and return in json format
def date_and_content(url):

    data = []
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
    date = article.publish_date
    title = article.title
    title_check = set()
    if title not in title_check:
        title_check.add(title)
        if is_not_blank(content):
            if date is None:
                data.append({
                    "Title": title,
                    "date": "no date found",
                    "Content": content,
                })

            else:
                date = date.strftime('%Y-%m-%d')

                data.append({
                    "Title": title,
                    "date": date,
                    "Content": content,
                })
    data2 = json.dumps(data, ensure_ascii=False).encode('utf8')
    return data2


def the_machine(original_url):
    url_set = get_articles_url(original_url)
    for url in url_set:
        dt = date_and_content(url)
        print(dt.decode())

# TESTING SECTION


origin_url = 'https://cnn.com'

#origin_url = 'https://cnn.com'

the_machine(origin_url)


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



