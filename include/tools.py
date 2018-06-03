# -*- coding: utf-8 -*-
import os

class tools_api:

	def isAscii(self, str):
		return all(ord(char) < 128 for char in str)

	def deleteRusWords(self, name):
		i = 0# i < 3
		while i < 6:
			j = 0
			while j < len(name):
				if self.isAscii(name[j]) == True:
					pass
				else:
					if i < 1:
						name = name[:j] + name[j+5:]
					else:
						name = name[:j] + name[j+1:]
				j += 1
			i += 1
		print("Your word: " + name)
		return name