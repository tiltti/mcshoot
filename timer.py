#!/usr/bin/python

import time
from threading import Timer
from colorama import init
from colorama import Fore, Back, Style

# init colorama
init(autoreset=True)

debug = True

# TODO: Change accordingly
# Times are in seconds
startDelay = 2
loadDelay = 3
attDelay = 7
varDelay = 4
stopDelay = 5

# Led definitions and display names

off = 'Off'
green = 'Green'
red = 'Red'
yellow = 'Yellow'

abortText = 'Abort'

def initTimer():
	if debug:
		print 'Timer initialized with values (secs):'
		print 'Start delay: ' + Fore.RED + '%s' % startDelay
		print 'Load delay: ' + Fore.RED + '%s' % loadDelay
		print 'Attention delay: ' + Fore.RED + '%s' % attDelay
		print 'Variable delay: ' + Fore.RED + '%s' % varDelay
		print 'Stop delay: ' + Fore.RED + '%s' % stopDelay
		print(Fore.RESET + Back.RESET + Style.RESET_ALL)
	t = Timer(startDelay, hello)

def startClock():
	changeLedStatus(off)

def changeLedStatus(status):
	ledStatus = status
	print 'Led status: %s' % ledStatus

def hello():
	print 'hello world'

def main():
	initTimer()
	startClock()


if __name__ == "__main__":
	main()

