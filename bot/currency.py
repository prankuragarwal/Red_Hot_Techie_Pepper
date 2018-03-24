import requests
import json

#convert eur to inr 
class curr(object):
	def __init__(self):
		self.url = 'https://currency-api.appspot.com/api/'

	def curfun(self, content):
		fr = content[3]
		to = content[5]
		if content[2] == "to":
			temp = to
			to = fr
			fr = temp
		#self.url = self.url + fr + '/' + to + '.json'
		self.r = requests.get(self.url+ fr + '/' + to + '.json')
		return float(self.r.json()["rate"])
