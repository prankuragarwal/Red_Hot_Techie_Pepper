import requests
#take place as argument in function
class Bus(object):
	def __init__(self):
		self.url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
		self.url2 = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyDJNoEuLGP2o2PYnRWOx29AvA0kOGQJZO4&location='

	def busfun(self, content):
		i = 2
		place = ""
		l = len(content)
		while (i < l):
			place += content[i] + " "
			i = i + 1
		#print(place)
		self.r = requests.get(self.url + place + ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU')
		results = self.r.json()
		#print(results)
		longitude = results["results"][0]["geometry"]["location"]["lat"]
		latitude = results["results"][0]["geometry"]["location"]["lng"]
		print(str(longitude))
		print(str(latitude))
		temp = self.url2 + str(longitude) + ',' + str(latitude) + '&rankby=distance&types=bus_station'
		self.r2 = requests.get(temp)
		results2 = self.r2.json()
		print(temp)
		print(results2)
		i = 0
		ans = ""
		for i in results2['results']:
			name = i['name']
			ans += name
			ans += "\n"
			vicinity = i['vicinity']
			ans += vicinity + "\n\n"
		print(ans)
		return ans