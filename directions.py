import json, urllib
from urllib.parse import urlencode
import googlemaps
import urllib.request
from sys import argv 
import pprint
from stripper import MLStripper
import re
#take start finish as argument in function

from html.parser import HTMLParser
p = pprint.PrettyPrinter()
class Direct(object):
    def __init__(self):
        self.url = 'http://maps.googleapis.com/maps/api/directions/json?'
        self.stripper = MLStripper()

    def strip_tags(self, html):
        self.stripper.feed(html)
        return self.stripper.get_data()

    def directfun(self, content):
        start = ""
        finish = ""
        i = 3
        l = len(content)
        while (i < l):
            if content[i].lower() == "to":
                i = i + 1
                break
            start += content[i] + " "
            i = i + 1
        start = start.strip()
        while (i < l) :
            finish += content[i] + " "
            i = i + 1
        finish = finish.strip()
        p.pprint(start)
        p.pprint(finish)
        newurl = 'https://maps.googleapis.com/maps/api/directions/json?%s&key=AIzaSyC33RfzIlcWI_Mq7YMNZFYJVhsrqKu1cPs' % urlencode((('origin', start), ('destination', finish)))
        #p.pprint(newurl)
        ur = urllib.request.urlopen(newurl)
        #p.pprint(ur)
        tem = ur.read()
        #p.pprint(tem)
        enc = ur.info().get_content_charset('utf8')
        result = json.loads(tem.decode(enc))
        #p.pprint(result)
        ans = ""
        #p.pprint(len(result['routes'][0]['legs'][0]['steps']))
        #p.pprint(result['routes'][0]['legs'][0]['steps'][0])
        for i in range (0,len(result['routes'][0]['legs'][0]['steps'])):
            j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
            #p.pprint(j)
            #p.pprint(strip_tags(j))
            #ans += strip_tags(j) + "\n"
            #ans += strip_tags(j)
            ans += re.sub('<[A-Za-z\/][^>]*>','', j) + "\n"
        if len(ans) == 0:
            ans = "No route found."

        return ans