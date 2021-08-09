import requests
from bs4 import BeautifulSoup
import datetime
from newspaper import Article
import json
number= ["1","2","3","4","5"]
url = 'https://edition.cnn.com/2021/08/09/politics/donald-trump-justice-department-elections-republicans/index.html'
# #url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
# article = Article(url)
# article.download()
# article.parse()
# article2 = article.text
# print(article2)

def date_and_content(url):
    data = []
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
    date = article.publish_date
    title = article.title
    print(date)
    data.append({
        "title": title,
        "date":date.isoformat(),
        "content": content,
    })
    data2 = json.dumps(data)
    return data2

dc = date_and_content(url)
print(dc)

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



