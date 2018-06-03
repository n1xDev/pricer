#https://market.yandex.ru/product/10495456/reviews?hid=91491&track=tabs
# -*- coding: utf-8 -*-
import os, sys, requests, time, json

from flask import Flask, request, send_from_directory, render_template
import numpy as np

sys.path.append("include")
import tools
from analyzer import analyzer_api

sys.path.append("include/shops")
from yandex import yandex_api
from e_katalog import e_katalog_api
from mailru import mailru_api
from dns import dns_api
from mvideo import mvideo_api

yandex_api_ = yandex_api()
e_katalog_api_ = e_katalog_api()
mailru_api_ = mailru_api()
mvideo_api_ = mvideo_api()
dns_api_ = dns_api()

analyzer_api_ = analyzer_api()

print("        !-- The Pricer Started --!")

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': '1' } # выдуманный пользователь
    return render_template("index.html")

@app.route('/more')
def more():
    user = { 'username': '2' } # выдуманный пользователь
    return render_template("info.html")

@app.route('/contacts')
def contacts():
    user = { 'username': '2' } # выдуманный пользователь
    return render_template("contacts.html")

@app.route('/analyze')
def analyze():
    user = { 'username': '2' } # выдуманный пользователь
    return render_template("analyze.html")

#################################################
@app.route('/analyze_data', methods=['POST'])
def analyze_data():
	result = request.form.get('category')
	if result == "smarts":
		return dns_api_.checkSmartphones()
	elif result == "phones":
		return dns_api_.checkPhones()
	else:
		return "err"

#################################################

@app.errorhandler(404)
def page_not_found(e):
    # your processing here
    return render_template("404.html")

if __name__ == "__main__":
    app.run()

'''mvideo_api_.checkSmartphones()
time.sleep(35)
dns_api_.checkSmartphones()'''