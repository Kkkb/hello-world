from urllib import request
import re

html = request.urlopen(
    "http://kkkb.github.io/css-beginner/static/spider-test.html"
).read().decode('utf-8')

res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)
print("\nPage paragraph is: ", res[0])

res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ",res)