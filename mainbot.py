import pprint
import zulip
import sys
import re
import json
import httplib2
import os
from chatterbot import ChatBot
from currency import curr
from lat_lon import latlon
from language import Lang
from restaurants import Rest
from bus_stations import Bus
from tourist_places import Tour
from autocorrect import spell
from jobs import Job
from directions import Direct
from atm import Atm
from autocorrect import spell
#from trainers import UbuntuCorpusTrainer
p = pprint.PrettyPrinter()
BOT_MAIL = "test-bot@prankuragarwal.zulipchat.com"

class ZulipBot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://prankuragarwal.zulipchat.com/api/")
		self.subscribe_all()
		self.chatbot = ChatBot("Test", trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
		#self.chatbot.train("chatterbot.corpus.english")
		#self.chatbot.train("chatterbot.corpus.english.greetings")
		#self.chatbot.train("chatterbot.corpus.english.conversations")
		self.currency = curr()
		self.lat_lon = latlon()
		self.language = Lang()
		self.restaurants = Rest()
		self.bus_stations = Bus()
		self.tourist_places = Tour()
		self.jobs = Job()

		self.directions = Direct()
		self.atm = Atm()
		self.subkeys = ["currency", "latilongi", "language", "restaurant", "bus", "tourist", "job", "direction","atm"]

	def urls(self, link):
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link)
		return urls

	def subscribe_all(self):
		json = self.client.get_streams()["streams"]
		streams = [{"name": stream["name"]} for stream in json]
		self.client.add_subscriptions(streams)

	def help(self):
		message = "**Welcome to Test Bot**\nTest Bot has various subfields\nType `test help <subfield>` to get help for specific subfield.\n"
		message += "\n**Subfields**\n"
		message += "`currency` - Get Currency\n"
		message += "`latilongi` - Get Latitude Longitude\n"
		message += "`restaurant` - Get Restaurant\n"
		message += "`bus` - Get Bus Stands\n"
		message += "`tourist` - Get Tourist Places\n"
		message += "`job` - Get Available Jobs nearby\n"
		message += "`direction` - Get Directions\n"
		message += "\nIf you're bored Talk to Omega Bot, it will supercharge you"
		return message
	def help_sub(self, key):
		key = key.lower()
		message = "**Usage**\n"
		if key == "currency":
			message += "`omega crypto <crypto-currency-code>` - To Get Price in USD\n"
			message += "`omage crypto <crypto-currency-code> in <currency>` - To Get Price in Specified Currency\n"
		elif key == "latilongi":
			message += "`omega translate <phrase to be translated>` - To Get Translate from Foreign Language to English\n"
		elif key == "restaurant":
			message += "`omega translate <phrase to be translated>` - To Get Translate from Foreign Language to English\n"
		elif key == "bus":
			message += "`omega translate <phrase to be translated>` - To Get Translate from Foreign Language to English\n"
		elif key == "tourist":
			message += "`omega translate <phrase to be translated>` - To Get Translate from Foreign Language to English\n"
		elif key == "job":
			message += "`omega translate <phrase to be translated>` - To Get Translate from Foreign Language to English\n"
		elif key == "direction":
			message += "`omega translate <phrase to be translated>` - To Get Translate from Foreign Language to English\n"
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

		print("yeah")

		if content[0].lower() == "testbot" or content[0] == "@**testbot**":
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
		elif "omega" in content and content[0] != "omega":
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
		print("Thanks for using Test Bot. Bye!")
		sys.exit(0)

