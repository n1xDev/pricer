# -*- coding: utf-8 -*-
import os, sys, requests, json
from bs4 import BeautifulSoup

sys.path.append("..")
from tools import tools_api

tools_api_ = tools_api()

class mvideo_api:

    smartphones = [[], []]

    def checkSmartphones(self):
        url = "http://www.mvideo.ru/smartfony-i-svyaz/smartfony-205/f/page=1?sort=priceLow"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'}
        response = requests.get(url, headers=headers)
        f = open('data/mvideo.html', 'w')
        f.write(response.content)
        f = open('data/mvideo.html', 'r')
        page = BeautifulSoup(f.read(), 'html.parser')
        page_quantity = page.findAll("a", {"class": "pagination-item-link "})
        i = 1
        while i < int(page_quantity[7].contents[0]):
            print("Parsing " + str(i) + " page")
            url = "http://www.mvideo.ru/smartfony-i-svyaz/smartfony-205/f/page=" + str(i) + "?sort=priceLow"
            response = requests.get(url, headers=headers)
            f = open('data/mvideo.html', 'w')
            f.write(response.content)
            f = open('data/mvideo.html', 'r')
            page = BeautifulSoup(f.read(), 'html.parser')
            devices = page.findAll("a", {"class" : "product-tile-title-link sel-product-tile-title"})
            prices = page.findAll("strong", {"class":"product-price-current sel-product-tile-price"})
            j = 0
            while j < 12:
                try:
                    current_device = devices[j].contents[0][10:]
                    if current_device[-3:-2] == ")":
                        k = 0
                        while k < len(current_device):
                            if current_device[-k : -k + 1] == "(":
                                current_device = current_device[:-k]
                            k += 1
                    self.smartphones[0].append(current_device)
                    self.smartphones[1].append(str(int(prices[j].contents[0])))
                    file_name = open("data/names.txt", 'a')
                    file_name.write(current_device + "\n")
                    file_name.close()
                    file_price = open("data/prices.txt", 'a')
                    file_price.write(str(int(prices[j].contents[0])) + "\n")
                    file_price.close()
                    '''with open('data/mvideo.json', 'w') as outfile:
                        json.dump(self.smartphones, outfile)'''
                except:
                    pass
                j += 1
            i += 1

    def checkPhones(self):
        pass