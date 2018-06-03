# -*- coding: utf-8 -*-
import sys, os, unicodedata, datetime

class analyzer_api:

	def checkPrice(self, curr_price, marks, start_date):
		# this method can correct product price
		pass

	def checkDate(self, start_date):
		# this method can give the time difference in days
		current_date = datetime.date.today()
		delta = current_date - start_date
		delta = str(delta)
		if delta[2] == " ":
			delta = delta[:2]
		else:
			delta = delta[:3]
		return delta

	def checkMarks(self, marks):
		# this method can give average mark after analyzing
		if not marks:
			return -1
		else:
			final_mark = (float((marks[0] * 2) + (marks[1] * 3) + (marks[2] * 4) + (marks[3] * 5))/float(marks[0] + marks[1] + marks[2] + marks[3]))
		return final_mark