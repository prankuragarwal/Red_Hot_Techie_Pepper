import requests
#take place as argument in function
class restaurants(object):
	def __init__(self):
		self.url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
		self.url2 = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='

	def restfun(self, content):

		self.r = requests.get(self.url + place + ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU')
		results = self.r.json()
		longitude = results["results"][0]["geometry"]["location"]["lat"]
		latitude = results["results"][0]["geometry"]["location"]["lng"]
		self.r = requests.get(self.url2 + latitude + ',' + longitude + '&radius=5000&types=restaurant&keyword=Restaurants&key= AIzaSyDJNoEuLGP2o2PYnRWOx29AvA0kOGQJZO4')
		results = self.r.json()
		i = 0
		ans = ""
		for i in results['results']:
			name = i['name']
		    #print (name)
		    ans += name + "\n"
		    try:
		        opened = i['opening_hours']
		        openedd=opened['open_now']
		        if openedd:
		            ans += "OPENED NOW\n"
		            #print ("OPENED NOW")
		        else:
		            ans += "CLOSED\n"
		            #print ("CLOSED")
		    except:
		        pass
		    try:
		        rating = i['rating']
		        ans += "Rating: " + rating + "\n"
		        #print (rating)
		    except:
		    	ans += "Rating not available\n"
		        pass
		    vicinity = i['vicinity']
		    ans += vicinity + "\n"
		    #print (vicinity+"\n")
		return ans