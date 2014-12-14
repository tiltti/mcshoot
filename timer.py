#!/usr/bin/python

import sys
import time
import getopt
from time import sleep
from threading import Timer
from colorama import init
from colorama import Fore, Back, Style

debug = False

# TODO: Set via cmd args or property file
# LCD size in characters
lcdSize = ('16','2')

# init colorama
init(autoreset=True)

# TODO: Change accordingly
# Times are in seconds
startDelay = 1
loadDelay = 1
attDelay = 1
varDelay = 1
stopDelay = 1

# Led definitions and display names

off = 'Off'
green = 'Green'
red = 'Red'
yellow = 'Yellow'

abortText = 'Abort'
output = 'screen'

color = False

class ShootUtils:
	def pythonTesti(self):
		print("foobar")
		return "foobar"

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
	runSequence('Start', startDelay, yellow)
	runSequence('Load', loadDelay, green)
	runSequence('Attention', attDelay, red)
	runSequence('Shoot', varDelay, green)
	runSequence('Stop/Unload', stopDelay, red)

def runSequence(delayName, delayTime, ledColor):
        lcdPrint(['Seq: ' + delayName, 'Led: ' + ledColor])
	print 'Sequence: ' + delayName + ', Led color: ' + ledColor
	s = 0
	while s < delayTime :
		s = s +1
		sys.stdout.write('.')
		sleep(1)
	sys.stdout.write('\n')

def changeLedStatus(status):
	ledStatus = status
	print 'Led status: %s' % ledStatus

def checkArguments():
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)

def finnish():
	lcdPrint(['Round complete!','Exiting...'])
	sys.exit()

def hello():
	print 'foo'

def lcdPrint(text):
        print Fore.YELLOW + Back.BLUE + '+----------------+'
	for index, line in enumerate(text):
		if len(line) > 16:
			print Fore.YELLOW + Back.RED + 'Too long string for LCD!'
		while len(line) < 16:
			line = line + ' '
		print Fore.YELLOW + Back.BLUE + '|' + line + '|'
        print Fore.YELLOW + Back.BLUE + '+----------------+'

def usage():
	print 'timer.py -o --output [ lcd | screen ] -c --color [ true | false ] -d --debug [ true | false ]'

def main(argv):
	global lcd
	global color
	global debug
	global lcdSize
	global output

  	try:
		opts, args = getopt.getopt(argv,"ho:c:d:",["output=","color=","debug="])
	except getopt.GetoptError:
    		usage()
		sys.exit(2)
   	
   	for opt, arg in opts:
      		if opt == '-h':
         		usage()
         		sys.exit()
      		elif opt in ("-o", "--output"):
			if arg.lower() == 'lcd': 
				output = 'lcd'
			elif arg.lower() == 'screen':
				output = 'screen'
         		else:
				usage()
				sys.exit(2)
      		elif opt in ("-c", "--color"):
         		if arg == 'true' or arg == 'True':
				color = True
			elif arg == 'false' or arg == 'False':
				color = False
			else:
				usage()
				sys.exit(2)
            	elif opt in ("-d", "--debug"):
                	if arg == 'true' or arg == 'True':
                		debug = True
                	elif arg == 'false' or arg == 'False':
                    		debug = False
                	else:
                    		usage()
                    		sys.exit(2)

	# main program
	if (debug):
		checkArguments()
                print 'Debug: %r' % debug
                print 'Output: %s' % output
                print 'Color: %r' % color
                print 'lcdSize: {0}'.format(lcdSize)
	resetColors()
	showLogo()
	initTimer()
	startClock()
	finnish()

if __name__ == "__main__":
	main(sys.argv[1:])

