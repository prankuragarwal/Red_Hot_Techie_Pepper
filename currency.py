import requests

a = input('Enter currency to convert from?')
a = a.upper()

b = input('Enter currency to convert to?')
b = b.upper()

c = float(input('Enter value to convert?'))

url = ('https://currency-api.appspot.com/api/%s/%s.json') % (a, b)
#print (url)

r = requests.get(url)
print (r.json()['rate'])

print (c*float(r.json()['rate']))


