#!/usr/bin/python

import sys
import time
from time import sleep
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

def resetColors():
	Fore.RESET
	Back.RESET
	Style.RESET_ALL

def showLogo():
	# made with: http://www.kammerl.de/ascii/AsciiSignature.php
        # font: cyberlarge
        print Fore.GREEN + '_______ _______ _______ _     _  _____   _____  _______'
        print Fore.GREEN + '|  |  | |       |______ |_____| |     | |     |    |   '
        print Fore.GREEN + '|  |  | |_____  ______| |     | |_____| |_____|    |   '

def initTimer():
	if debug:
		print 'Timer initialized with values (secs):'
		print 'Start delay: ' + Fore.RED + '%s' % startDelay
		print 'Load delay: ' + Fore.RED + '%s' % loadDelay
		print 'Attention delay: ' + Fore.RED + '%s' % attDelay
		print 'Variable delay: ' + Fore.RED + '%s' % varDelay
		print 'Stop delay: ' + Fore.RED + '%s' % stopDelay
	resetColors()
	t = Timer(startDelay, hello)

def startClock():
	runSequence('Start', startDelay, red)
	runSequence('Load', loadDelay, red)
	runSequence('Attention', attDelay, yellow)
	runSequence('Shoot', varDelay, green)
	runSequence('Stop', stopDelay, red)


def runSequence(delayName, delayTime, ledColor):
	print '\nSequence: ' + delayName + ', Led color: ' + ledColor
	s = 0
	while s < delayTime :
		s = s +1
		sys.stdout.write('.')
		sleep(1)


def changeLedStatus(status):
	ledStatus = status
	print 'Led status: %s' % ledStatus

def hello():
	print 'hello world'

def main():
	resetColors()
	showLogo()
	initTimer()
	startClock()

if __name__ == "__main__":
	main()

