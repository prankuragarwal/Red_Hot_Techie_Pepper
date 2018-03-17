import requests
url='https://jobs.github.com/positions.json?location=India'
#+place
r = requests.get(url)
results = r.json()
#print (results)
i=0;
#if (bool(results)=="True"):
for i in results:
    created = i['created_at']
    print (created)
    title = i['title']
    print (title)
    print (i['url']+"\n")
#else:
 #   print ("No Jobs available in your location")
