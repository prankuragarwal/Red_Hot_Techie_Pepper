import requests

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
		#print(self.url + place)
		results = self.r.json()

		i = 0
		ans = ""
		print(results)
		print(self.url + place)
		for i in results:
			created = i['created_at']
			ans += created + "\n"
			title = i['title']
			ans += title + "\n"
			ans += i['url'] + "\n"
		if ans == "":
			ans = "No jobs available at your location"

		return ans
