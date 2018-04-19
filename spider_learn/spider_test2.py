from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://kkkb.github.io/css-beginner/static/spider-test.html").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
print(soup.h1)

print('\n', soup.p)

all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)