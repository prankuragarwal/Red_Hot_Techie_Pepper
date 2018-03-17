import requests
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' +place+ ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU'
r = requests.get(url)
results = r.json()
longitude = results["results"][0]["geometry"]["location"]["lat"]
latitude = results["results"][0]["geometry"]["location"]["lng"]
url1='https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyDJNoEuLGP2o2PYnRWOx29AvA0kOGQJZO4&location=25.4930,81.8639&rankby=distance&types=bus_station'
r1 = requests.get(url1)
results = r1.json()
print(results)
i=0
for i in results['results']:
    name = i['name']
    print (name)
    vicinity = i['vicinity']
    print (vicinity+"\n")
