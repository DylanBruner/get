import requests as req
from datetime import datetime
import time as ptime

now = datetime.now()


def lock():
	con = req.get("http://192.168.50.110/lock")

def unlock():
	con = req.get("http://192.168.50.110/unlock")


def checkTime():
	hour = now.strftime("%I")
	mn = now.strftime("%M")
	ap = now.strftime("%p")
	if int(hour) <= 8 and str(ap) == "AM":
		relayOff()
	elif int(hour) <= 8 and str(ap) == "PM":
		relayOn()


def relayOn():
	print("[!] Turning pump on")
	req.get("http://192.168.50.110/4/on")


def relayOff():
	print("[!] Turning pump off")
	req.get("http://192.168.50.110/4/off")


while True:
	checkTime()
	ptime.sleep(5)
