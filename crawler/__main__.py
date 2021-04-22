import urllib.request
from wikicrawler import WikiCrawler
from collections import OrderedDict
import re

url = urllib.request.urlopen('https://en.wikipedia.org/wiki/Microsoft')
html = url.read().decode()
url.close()
section = "History"
default_display_count = 10

display_count = input('Set a word limit (Default: 10):\n')
while True:
	try:
		if len(display_count) <= 0:
			display_count = default_display_count
			break

		if len(display_count) > 0:
			display_count = int(display_count)
			break
	except:
		display_count = input('Please add a valid number:\n')
display_count = (default_display_count, display_count)[display_count >= 0]

# get the second input and verify it's a string
excluded_words = input('Any words that need to be excluded (Space or comma separated):\n')
if len(excluded_words) > 0:
	excluded_words = re.split('[ ,]', excluded_words)
excluded_words = list(filter(lambda word: len(word) > 0, excluded_words))



crawl = WikiCrawler()
crawl.section = section
crawl.feed(html)

data = crawl.data.items()

ordered_and_trim_list = OrderedDict(sorted(data, key=lambda x: x[1], reverse=True)[:display_count])

for key, val in ordered_and_trim_list.items():
	print(f"{key:>11}: {val}")
