import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import datetime
from newspaper import Article
import json
from newspaper import build
import os

#check if string is not blank
def is_not_blank(s):
    return bool(s and not s.isspace())


#This function returns all the url found in base url given: ie
# 'https://vnexpress.net', 'https://cnn.com'...
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
        single_dict = {}
        if title not in title_check and type(content) == str and len(content) > 1:
            title_check.add(title)
            if is_not_blank(content):
                if date is None and article is not None:
                    single_dict ={
                        "title": title,
                        "date": "no-date-found",
                        "content": content,
                        "url": url
                    }
                    data.append(single_dict)
                else:
                    date = date.strftime('%Y-%m-%d')
                    single_dict = {
                        "title": title,
                        "date": date,
                        "content": content,
                        "url": url
                    }
                    data.append(single_dict)
            return data
    except Exception as e:
        print(e)


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
        dt = date_and_content(url)
        if dt is not None:
            data.append(dt)
            print(counter + 10)
            counter += 1

        if(counter == 50):
            #data2 = json.dumps(data, ensure_ascii=False).encode('utf8')
            #return data
            save_to_file(data)

            return 0


def save_to_file(results):
    print('Gathering data')
    counter = 0
    parent = 'C:/Users/Thinh/PycharmProjects/crawl_test/'
    for result in results:
        url = result[0]['url']
        print(url)
        title = result[0]['title']
        print(title)
        pathz = url.split("/")[-1]
        if (len(pathz) < 15):
            pathz = url.split("/")[-2]
        #CNN dung-2

        domain = urlparse(url).netloc
        date = result[0]['date']
        print(date)
        directory = domain + '/' + date
        path = os.path.join(parent, directory)
        file_name = pathz + '.json'
        newpath = path + "/" + file_name
        print(counter)
        counter += 1
        if not os.path.exists(path):
            #make new date file
            os.makedirs(path)
            with open(newpath, 'w') as outfile:
                json.dump(result, outfile)
        else:
            if not os.path.exists(newpath):
                with open(newpath, 'w') as outfile:
                    json.dump(result, outfile)




#date/tuoitre.vn/filejson

# TESTING SECTION
#
#origin_url = 'https://vnexpress.net'
#vnexpress returns no date
origin_url = 'https://www.foxnews.com/'
#origin_url = 'https://zingnews.vn/'
#zingnews got some errors

#origin_url = 'https://www.cnn.com/'
#same error with zing

#results = the_machine(origin_url)
#data = json.loads(results)
i = 4
y = 66
print(f'{i}+{y} = {i+y}')
