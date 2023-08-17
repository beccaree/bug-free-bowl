import requests
from bs4 import BeautifulSoup

# thanks >> https://stackoverflow.com/questions/75413623/python-web-scrapping-get-html-links-from-within-a-specific-div-and-from-sub-pag

# input: title page url
targetUrl = 'https://czbooks.net/n/c65cll'

page = requests.get(targetUrl)
page.raise_for_status()
soup = BeautifulSoup(page.content, 'html.parser')

# book info
infoSection = soup.find('div', class_='info')
title = infoSection.find('span', class_='title').text.strip()
author = infoSection.find('span', class_='author').find('a').text.strip()
print(title + ' by ' + author)

# write chapters to files
chapters = soup.find('ul', id='chapter-list')
assert chapters, 'chapters not found'

with open('book.txt', 'w', encoding='utf-8') as f:

    for c in chapters.find_all('a', href=True):
        cTitle = c.text.strip()
        cUrl = c['href']

        cPage = requests.get('https:' + cUrl)
        cPage.raise_for_status()
        cSoup = BeautifulSoup(cPage.content, 'html.parser')
        
        contentDiv = cSoup.find('div', class_='content')
        assert contentDiv, 'could not find content for ' + cTitle
        f.write(contentDiv.text)
        f.write('\n\n')

print('find ' + title + ' at book.txt')
