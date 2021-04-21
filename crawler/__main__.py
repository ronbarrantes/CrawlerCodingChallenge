import urllib.request
from wikicrawler import WikiCrawler
from collections import OrderedDict

url = urllib.request.urlopen('https://en.wikipedia.org/wiki/Microsoft')
html = url.read().decode()
url.close()
section = "History"
frequency = 10

crawl = WikiCrawler()
crawl.section = section
crawl.feed(html)

ordered_and_trim_list = OrderedDict(sorted(crawl.data.items(), key=lambda x: x[1], reverse=True)[:frequency])

for key, val in ordered_and_trim_list.items():
	print(f"{key:>9}: {val}")