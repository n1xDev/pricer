# -*- coding: utf-8 -*-
import xlrd, xlutils, unicodedata, sys, json
from e_katalog import e_katalog_api

sys.path.append("..")
from tools import tools_api

e_katalog_api_ = e_katalog_api()
tools_api_ = tools_api()

class dns_api:
	db = xlrd.open_workbook('data/dns.xls',formatting_info=True)

	smartphones = [[], []]
	phones = [[], []]

	answ = [[], []]

	def checkSmartphones(self):
		sheet = self.db.sheet_by_index(4)
		val = sheet.row_values(0)[0]
		vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
		res = [[], []]
		i = 100 # i = 23
		while i < 200: # < 485
			self.smartphones[0].append(vals[i][2].encode('utf-8'))
			self.smartphones[1].append(vals[i][22])
			i += 1
		i = 0
		while i < len(self.smartphones[0]) - 1:
			curr_phone = self.smartphones[0][i]
			if curr_phone[1] == ".":
				curr_phone = curr_phone[22:]
			else:
				curr_phone = curr_phone[20:]
			curr_phone = tools_api_.deleteRusWords(curr_phone)
			#e_katalog_api_.checkMobile(self.smartphones[0][i], self.smartphones[1][i])
			answ_marks = e_katalog_api_.checkMobile(curr_phone, self.smartphones[1][i])
			self.answ[0].append(curr_phone)
			self.answ[1].append(answ_marks)
			i += 1
		self.answ = json.dumps(self.answ)
		return self.answ

	def checkPhones(self):
		sheet = self.db.sheet_by_index(4)
		val = sheet.row_values(0)[0]
		vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
		i = 487
		while i < 614:
			self.phones[0].append(vals[i][2].encode('utf-8'))
			self.phones[1].append(vals[i][22])
			i += 1
		return "phones will be soon..."