from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://github.com/Kkkb/hello-world").read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')

article_tag = soup.find("article")
a_tag = article_tag.find_all("a")

for l in [l['href'] for l in a_tag if '#' not in l['href']]:
    print(l)