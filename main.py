import requests
from bs4 import BeautifulSoup

number= ["1","2","3","4","5"]
for i in range(5):
    url = "https://www.bbc.co.uk/search?q=crypto+currency&page="

    new_link = url + number[i]
    print(new_link)
    response = requests.get(new_link)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all('div', class_='ssrcss-1cbga70-Stack e1y4nx260')


    for article in articles:
        title = article.find('span',{"aria-hidden":"false"})

        link = article.find('a').attrs["href"]
        print('\n')
        print(title.get_text())
        print (link)
        print ("--------------------")

# response = requests.get("https://www.bbc.co.uk/search?q=crypto+page")
# soup = BeautifulSoup(response.content, "html.parser")
# articles = soup.find_all('div', class_='ssrcss-1cbga70-Stack e1y4nx260')
#
#
# for article in articles:
#     title = article.find('span',{"aria-hidden":"false"})
#
#     link = article.find('a').attrs["href"]
#     print('\n')
#     print(title.get_text())
#     print (link)
#     print ("--------------------")

