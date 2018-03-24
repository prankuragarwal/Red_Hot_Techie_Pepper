import pprint
import zulip
import sys
import re
import json
import httplib2
import os
from chatterbot import ChatBot
from currency import curr
#from lat_lon import latlon
from language import Lang
from restaurants import Rest
from bus_stations import Bus
from tourist_places import Tour
from autocorrect import spell
from jobs import Job
from directions import Direct
from atm import Atm
#from autocorrect import spell
#from trainers import UbuntuCorpusTrainer
p = pprint.PrettyPrinter()
BOT_MAIL = "i-bot@rhtp.zulipchat.com"

def dhelp():
	message = "**Welcome to I-BOT**\nIBOT has various subfields\nType `ibot help <subfield>` to get help for specific subfield.\n"
	message += "\n**Subfields**\n"
	message += "`currency` - Get currency conversion rate\n"
	message += "`atm` - Get addresses of nearby ATM(s)\n"
	message += "`restaurant` - Get addresses of nearby restaurant(s)\n"
	message += "`bus` - Get addresses of nearest bus stand(s)\n"
	message += "`tourist` - Get addresses of nearby tourist place(s)\n"
	message += "`job` - Get a list of jobs available nearby\n"
	message += "`direction` - Get directions from one place to other\n"
	message += "`language` - Translate your English sentences to other languages\n"
	message += "\nIf you're bored Talk to IBOT, it will supercharge you"
	return message

class ZulipBot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://rhtp.zulipchat.com/api/")
		self.subscribe_all()
		self.chatbot = ChatBot("Test", trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
		#self.chatbot.train("chatterbot.corpus.english")
		#self.chatbot.train("chatterbot.corpus.english.greetings")
		#self.chatbot.train("chatterbot.corpus.english.conversations")
		self.currency = curr()
		#self.lat_lon = latlon()
		self.language = Lang()
		self.restaurants = Rest()
		self.bus_stations = Bus()
		self.tourist_places = Tour()
		self.jobs = Job()

		self.directions = Direct()
		self.atm = Atm()
		self.subkeys = ["currency", "language", "restaurant", "bus", "tourist", "job", "direction","atm"]
		#mesg = dhelp()
		#self.client.send_message({
		#	"type": "stream",
		#	"content" : self.mesg
		#	})

	def urls(self, link):
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link)
		return urls

	def subscribe_all(self):
		json = self.client.get_streams()["streams"]
		streams = [{"name": stream["name"]} for stream in json]
		self.client.add_subscriptions(streams)

	def help(self):
		message = "**Welcome to I-BOT**\nIBOT has various subfields\nType `ibot help <subfield>` to get help for specific subfield.\n"
		message += "\n**Subfields**\n"
		message += "`currency` - Get currency conversion rate\n"
		message += "`atm` - Get addresses of nearby ATM(s)\n"
		message += "`restaurant` - Get addresses of nearby restaurant(s)\n"
		message += "`bus` - Get addresses of nearest bus stand(s)\n"
		message += "`tourist` - Get addresses of nearby tourist place(s)\n"
		message += "`job` - Get a list of jobs available nearby\n"
		message += "`direction` - Get directions from one place to other\n"
		message += "`language` - Translate your English sentences to other languages\n"
		message += "\nIf you're bored Talk to IBOT, it will supercharge you"
		return message
	def help_sub(self, key):
		key = key.lower()
		message = "**Usage**\n"
		if key == "currency":
			message += "`ibot currency from <currency code - 1> to <currency code - 2>` - To get currency conversion rate.\n"
		elif key == "atm":
			message += "`ibot atm <nearby location>` - To get addresses of nearby ATM(s).\n"
		elif key == "restaurant":
			message += "`ibot restaurant <nearby location>` - To get addresses of nearby restaurant(s).\n"
		elif key == "bus":
			message += "`ibot bus <nearby location>` - To get addresses of nearby bus stand(s).\n"
		elif key == "tourist":
			message += "`ibot tourist <nearby location>` - To get addresses of nearby tourist place(s).\n"
		elif key == "job":
			message += "`ibot job <nearby location>` - To get a list of jobs available nearby.\n"
		elif key == "direction":
			message += "`ibot direction from <source> to <destination>` - To get directions from one place to another.\n"
		elif key == "language":
			message += "`ibot language to <language name>` - To translate your English sentences to other languages.\n"
		else:
			message = self.help()
			message += "\n{} is not a valid subfield\n".format(key)
		return message		

	def process(self, msg):
		content = msg["content"].split()
		sender_email = msg["sender_email"]
		ttype = msg["type"]
		stream_name = msg['display_recipient']
		stream_topic = msg['subject']

		print(content)
		l = len(content)
#		temstr = spell(content[1].lower())
#		content[1] = temstr
#		print(content[1])
		if sender_email == BOT_MAIL:
			return 

		print("doing")

		if content[0].lower() == "ibot" or content[0] == "@**IBOT**":
			if content[1].lower() == "currency":
				message = self.currency.curfun(content)
				#print(message)
				self.client.send_message({
					"type": "stream",
					"subject" : msg["subject"],
					"to" : msg["display_recipient"],
					"content" : message
					})
			if content[1].lower() == "latilongi":
				message = self.lat_lon.latlonfun(content)
				#print(message)
				self.client.send_message({
					"type": "stream",
					"subject" : msg["subject"],
					"to" : msg["display_recipient"],
					"content" : message
					})
			if content[1].lower() == "language":
				message = self.language.langconvert(content)
				#print(message)
				self.client.send_message({
					"type": "stream",
					"subject" : msg["subject"],
					"to" : msg["display_recipient"],
					"content" : message
					})
			if content[1].lower() == "restaurant":
				message = self.restaurants.restfun(content)
				#print(message)
				self.client.send_message({
					"type": "stream",
					"subject" : msg["subject"],
					"to" : msg["display_recipient"],
					"content" : message
					})
			if content[1].lower() == "bus":
				message = self.bus_stations.busfun(content)
				#print(message)
				self.client.send_message({
					"type": "stream",
					"subject" : msg["subject"],
					"to" : msg["display_recipient"],
					"content" : message
					})
			if content[1].lower() == "tourist":
				message = self.tourist_places.tourfun(content)
				#print(message)
				self.client.send_message({
					"type": "stream",
					"subject" : msg["subject"],
					"to" : msg["display_recipient"],
					"content" : message
					})
			if content[1].lower() == "job":
				message = self.jobs.jobfun(content)
				#print(message)
				self.client.send_message({
					"type": "stream",
					"subject" : msg["subject"],
					"to" : msg["display_recipient"],
					"content" : message
					})
			if content[1].lower() == "atm":
				message = self.atm.atmfun(content)
				#print(message)
				self.client.send_message({
					"type": "stream",
					"subject" : msg["subject"],
					"to" : msg["display_recipient"],
					"content" : message
					})
			if content[1].lower() == "direction":
				message = self.directions.directfun(content)
				#print(message)
				self.client.send_message({
					"type": "stream",
					"subject" : msg["subject"],
					"to" : msg["display_recipient"],
					"content" : message
					})
			if content[1].lower() == "help" and len(content) == 2:
				message = self.help()
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message  
					})
			if content[1].lower() == "help" and len(content) > 2:
				subkey = content[2]
				message = self.help_sub(subkey)
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message  
					})
            
			if content[1] not in self.subkeys:
				ip = content[1:]
				ip = " ".join(ip)
				message = self.chatbot.get_response(ip).text
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})
             
		if self.urls(" ".join(content)):
			summary = self.w.wiki(" ".join(content))
			if summary:
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": summary
					})
		elif "ibot" in content and content[0] != "ibot":
			self.client.send_message({
				"type": "stream",
				"subject": msg["subject"],
				"to": msg["display_recipient"],
				"content": "Alas! Finally you called me :blush:"
				})
		else:
			return

def main():
	bot = ZulipBot()
	bot.client.call_on_each_message(bot.process)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Thanks for using IBOT. Bye!")
		sys.exit(0)

