from html.parser import HTMLParser
import re

class WikiCrawler(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.should_record = False
		self.data = {}
		self.section = ""

	def handle_starttag(self, tag, attrs):
		if tag == "span":
			for attr, val in attrs:
				if attr == 'id' and val == self.section:
					self.should_record = True

		if tag == 'h2' and self.should_record == True:
			self.should_record = False

	def handle_data(self, data):
		if self.should_record == True:
			temp_data = data.split()
			for i in range(len(temp_data)):
				word = temp_data[i]
				if re.match('[a-zA-Z]', word):
					if word in self.data.keys():
						self.data[word] = self.data[word] + 1
					else: 
						self.data[word] = + 1