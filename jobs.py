import requests
import json
import pprint
import urllib.request

p = pprint.PrettyPrinter()

class Job(object):
	def __init__(self):
		self.url = 'https://jobs.github.com/positions.json?location='
#+place
	def jobfun(self, content):
		i = 2
		place = ""
		l = len(content)
		while (i < l):
			place += content[i] + " "
			i = i + 1
		#self.r = requests.get(self.url + place)
		#print(self.r)
		p.pprint(self.url + place)
		ur = urllib.request.urlopen(self.url + place)
		tem = ur.read()
		enc = ur.info().get_content_charset('utf8')
		re = json.loads(tem.decode(enc))
		i = 0
		ans = ""
		p.pprint(re)
		#print(self.url + place)
		i = 0
		for i in re:
			created = i['created_at']
			ans += created + "\n"
			title = i['title']
			ans += title + "\n"
			ans += i['url'] + "\n"
		if ans == "":
			ans = "No jobs available at your location"

		return ans
