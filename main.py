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
    #print(url_set)
    return url_set


#This function  return date, content, and article's title
# and return in json format
def date_and_content(url):
    try:

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
                if date is None and article is not None:
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

        return data

    except:
        print('out of lines')


def the_machine(original_url):
    data = []
    print('Machine is working\n')
    url_set = get_articles_url(original_url)
    #print(url_set)
    print('Gathering data\n')
    print("Url set!\n")
    checker = True
    counter = 0
    for url in url_set:
        if checker:
            dt = date_and_content(url)
            data.append(dt)
            counter += 1
        if(counter == 20):
            checker= False
            data2 = json.dumps(data, ensure_ascii=False).encode('utf8')
            return data2







# TESTING SECTION


#origin_url = 'https://plo.vn/'

origin_url = 'https://www.foxnews.com/'

results = the_machine(origin_url)
data = json.loads(results)
print('System: getting result')
#for result in results:
for result in data:
    print(result)




