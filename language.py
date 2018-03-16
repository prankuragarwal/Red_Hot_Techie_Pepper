import json
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator
from gtts import gTTS
import os

class Lang(object):
	def __init__(self):
		self.language_translator = LanguageTranslator(username='5108690a-238a-4810-93bf-e2741f4487e3', password='JsAOmfm0XIwP')

	def langconvert(self, content):
		to = content[3].lower();
		toc = "en"
		if to == "english":
			toc = "en"
		elif to == "chinese":
			toc = "zh"
		elif to == "arabic":
			toc = "ar"
		elif to == "french":
			toc = "fr"
		elif to == "german":
			toc = "de"
		elif to == "italian":
			toc = "it"
		elif to == "japanese":
			toc = "ja"
		elif to == "portuguese":
			toc = "pt"
		elif to == "korean":
			toc = "ko"
		elif to == "spanish":
			toc = "es"
		else:
			toc = "lol"
		ans = ""
		if toc == "lol":
			ans = "Invalid Translation. Please try again."
		else:
			l = len(content)
			i = 4
			data = ""
			while (i < l):
				data += content[i]
				data += " "
				i = i + 1
			translation = self.language_translator.translate(text=data, source='en', target=toc)
			ans = translation["translations"][0]["translation"]
			myobj = gTTS(text=ans, lang=toc, slow=False)
			myobj.save("welcome.mp3")
			os.system("mpg321 welcome.mp3")
		return ans
