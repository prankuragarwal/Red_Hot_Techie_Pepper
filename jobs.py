import requests
import json

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
		self.r = requests.get(self.url + place)
		print(self.r)
		#print(self.url + place)
		results = self.r.text
		re = json.loads(results)
		i = 0
		ans = ""
		print(re)
		print(self.url + place)
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
