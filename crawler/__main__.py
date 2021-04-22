import urllib.request
from wikicrawler import WikiCrawler
from collections import OrderedDict

url = urllib.request.urlopen('https://en.wikipedia.org/wiki/Microsoft')
html = url.read().decode()
url.close()
section = "History"
default_display_count = 10
exclude_words = []

# get the first input and verify it's an int
display_count = input('Set a word limit: (Default: 10)\n')
while True:
	try:
		if len(display_count) < 0:
			display_count = default_display_count
			break

		if len(display_count) >= 0:
			display_count = int(display_count)
			break

	except:
		display_count = input('Please add a valid number:\n')



print(int(display_count))
display_count = (default_display_count, display_count)[display_count >= 0]











# get the second input and verify it's a string



crawl = WikiCrawler()
crawl.section = section
crawl.feed(html)

# filtered_items = 

ordered_and_trim_list = OrderedDict(sorted(crawl.data.items(), key=lambda x: x[1], reverse=True)[:display_count])

for key, val in ordered_and_trim_list.items():
	print(f"{key:>11}: {val}")
