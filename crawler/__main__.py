import urllib.request
from wikicrawler import WikiCrawler

url = urllib.request.urlopen('https://en.wikipedia.org/wiki/Microsoft')
html = url.read().decode()
url.close()
section = "History"

crawl = WikiCrawler()
crawl.section = section
crawl.feed(html)



# DELETE ALL THE STUFF ON THE BOTTOM

f = open('./dump.txt', 'w')
f.write(str(crawl.data))





print('all done')