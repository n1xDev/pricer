# -*- coding: utf-8 -*-
import os, requests
from bs4 import BeautifulSoup

class e_katalog_api:

	def getMarks(self, page):
		marks = []
		curr_mark = page.findAll("sub")
		i = 0
		while i < 4:
			print("now mark id = " + str(i))
			try:
				marks.append(int(curr_mark[i].contents[0]))
			except:
				pass
			i += 1
		return marks

	def checkFound(self, page):
		not_found = page.findAll("nobr")
		if not_found[0].contents[0].encode('utf-8') == 'не найдено ни одного товара':
			return False
		else:
			return True

	def checkMobile(self, name, price):
		print("Passed: " + name + " (" + str(price) + ")")
		url = 'http://www.e-katalog.ru/ek-list.php?search_=' + name + '&katalog_from_search_=122&search_but_='
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'}
		response = requests.get(url, headers=headers)
		f = open('data/e_katalog.html', 'w')
		f.write(response.content)
		f = open('data/e_katalog.html', 'r')
		page = BeautifulSoup(f.read(), 'html.parser')
		if self.checkFound(page) == True:
			print(self.getMarks(page))
			return self.getMarks(page)
		else:
			print("This product is not found.")
			return "err"