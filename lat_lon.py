import requests
import json

class latlon(object):
	def __init__(self):
		self.url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' +'350 Fifth Avenue New York, NY'+ ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU'

	def latlonfun(self, content):
		self.r = requests.get(self.url)
		results = self.r.json()
		longitude = results["results"][0]["geometry"]["location"]["lat"]
		latitude = results["results"][0]["geometry"]["location"]["lng"]
		return longitude, latitude