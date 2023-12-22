import bs4, requests
from fake_headers import Headers
KEYWORDS = ['база', 'сотрудник', 'Internet', 'Fighters ']
URL = "https://habr.com/ru/all/"
HEADERS = Headers(headers= True).generate()

response = requests.get(URL, headers=HEADERS)
soup = bs4.BeautifulSoup(response.text, features="html.parser")
articles = soup.find_all("article", class_='tm-articles-list__item')
for article in articles:
     date = article.find('time').text
     title = article.find('a', class_='tm-article-snippet__title-link').find("span").text
     preview = article.find(class_="article-formatted-body").text
     href = article.find(class_="tm-article-snippet__title-link").attrs.get('href')
     for word in KEYWORDS:
         if word in preview.split():
            print(f'Дата: {date} - Заголовок: {title} - Ссылка: {URL}{href}')
    