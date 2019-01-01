import requests
import time
from bs4 import BeautifulSoup
from Foundation import NSUserNotification
from Foundation import NSUserNotificationCenter
from Foundation import NSUserNotificationDefaultSoundName

country_being_followed = "IND"


def getCurrentMatches():
	BASE_URL = "http://www.cricbuzz.com/cricket-match/live-scores"
	return requests.get(BASE_URL)


def processResponse():
	response = getCurrentMatches()
	data = BeautifulSoup(response.content,"lxml")
	for match in data.find_all("a", {"class":"cb-lv-scrs-well-live"}):
		if (' won ' not in match.text) and (country_being_followed in match.text):
			showNotification(match)
			

def showNotification(match):
	notification = NSUserNotification.alloc().init()
	notification.setTitle_("Stumped!")
	notification.setInformativeText_(match.text)
	center = NSUserNotificationCenter.defaultUserNotificationCenter()
	center.deliverNotification_(notification)
 			


while(True):
	processResponse()
	time.sleep(5)
