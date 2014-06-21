#!/usr/bin/python

import time
from threading import Timer

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
		print 'Timer initialized with values:'
		print 'Start delay: %s sec' % startDelay
		print 'Load delay: %s sec' % loadDelay
		print 'Attention delay: %s sec' % attDelay
		print 'Variable delay: %s sec' % varDelay
		print 'Stop delay: %s sec' % stopDelay
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

