# -*- coding: utf-8 -*-
import os, requests
from bs4 import BeautifulSoup

class mailru_api:
	def CheckMobile(self, name, price):
		pass

	def Prepare(self):
		print("Preparing MailRU...")
		url = 'http://torg.mail.ru/mobilephones/apple-iphone-se-64gb-id14409831/'
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'}
		response = requests.get(url, headers=headers)
		f = open('data/mailru.html', 'w')
		f.write(response.content)
		f = open('data/mailru.html', 'r')
		page = BeautifulSoup(f.read(), 'html.parser')
		p = page.findAll("meta", { "itemprop" : "lowPrice" })
		i = 0
		while i < 9999:
			response = requests.get(url, headers=headers)
			f = open('data/mailru.html', 'w')
			f.write(response.content)
			f = open('data/mailru.html', 'r')
			print("trying: " + str(i))
			page = BeautifulSoup(f.read(), 'html.parser')
			p = page.findAll("meta", { "itemprop" : "lowPrice" })
			print(p[0].contents[1]['content'].encode('utf-8'))
			i += 1

		'''i = 0
		while i < 5:
			print(str(i+1) + "* -> " + p[i].contents[0].encode('utf-8'))
			i += 1'''

		#p = page.findAll("meta", { "class" : "ratingValue"})
		print(p)
		print("MailRU done.")