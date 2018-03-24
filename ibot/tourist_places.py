import requests
from sys import argv
#take place as argument in function
class Tour(object):
    def __init__(self):
        self.url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='

    def tourfun(self, content):
        i = 2
        place = ""
        l = len(content)
        while (i < l):
            place += content[i] + " "
            i = i + 1
        #print(place)
        self.r = requests.get(self.url + place + 'point+of+interest&key= AIzaSyDJNoEuLGP2o2PYnRWOx29AvA0kOGQJZO4')
        results = self.r.json()
        #print(results)
        longitude = results["results"][0]["geometry"]["location"]["lat"]
        latitude = results["results"][0]["geometry"]["location"]["lng"]
        i = 0
        ans = ""
        for i in results['results']:
            address = i['formatted_address']
            name = i['name']
            ans += name
            ans += "\n"
            try:
                opened = i['opening_hours']
                openedd = opened['open_now']
                if openedd:
                    ans += "OPENED NOW\n"
                else:
                    ans += "CLOSED\n"
            except:
                pass
            ans += address + "\n\n"
#		if ans == "" :
#			ans = "No results"
        #print(ans)
        return ans



