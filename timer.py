import time
from threading import Timer

# TODO: Change accordingly
startDelay = 2
shootDelay = 3

# Led definitions and display names

off = 'Off'
green = 'Green'
red = 'Red'
yellow = 'Yellow'

abortText = 'Abort'

def initTimer():
	print 'Timer initialized with values:'
	print 'Start delay: %s' % startDelay
	print 'Shoot delay: %s' % shootDelay
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

