#!/usr/bin/python
#
# Mcshoot made by Ossi Tiltti (github.com/tiltti)
# Using Menu.py made by Daniel Juenger (github.com/sleeepyjack)
# Using Adafruit_CharLCDPlate library by Adafruit Industries (github.com/adafruit)

# dependencies: Colorama

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from menu import Menu
from subprocess import *
from time import sleep, strftime
from threading import Timer
from colorama import init, Fore, Back, Style
import ConfigParser
import sys
import time
import getopt

lcd = Adafruit_CharLCDPlate()
menu = Menu()

configName = "mcshoot.cfg"

global startDelay

if __name__ == "main":
	main(sys.argv[1:])

def load_config(configFile):

	global debug
	global startDelay
	global loadDelay
	global attDelay
	global varDelay
	global stopDelay

	config = ConfigParser.RawConfigParser()
	config.read(configFile)

	debug = config.getboolean('Debug', 'debug')

	startDelay = str(config.getint('McShoot', 'startDelay'))
	loadDelay  = str(config.getint('McShoot', 'loadDelay'))
	attDelay   = str(config.getint('McShoot', 'attDelay'))
	varDelay   = str(config.getint('McShoot', 'varDelay'))
	stopDelay  = str(config.getint('McShoot', 'stopDelay'))

	if (debug):
		print "Debugging mode ENABLED!"
		print "startDelay: " + str(startDelay)
		print "loadDelay: " + str(loadDelay)
		print "attDelay: " + str(attDelay)
		print "varDelay: " + str(varDelay)
		print "stopDelay: " + str(stopDelay)

load_config(configName)

def dprint(text):
	if (debug):
		print text

# Utility function for runnin shell commands
def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
	return output


# The menu can show strings, bash and python expressions
#
#           topElement(      Top row Name, Type    , Low row content
#                           max 16 chars
#                       <-------x-------->            <-------x------->
top1  = menu.topElement("<   Network    >", "STRING", "       v       ")
top2  = menu.topElement("<   System     >", "STRING", "       v       ")
top3  = menu.topElement("<   Alkuviive  >", "STRING", startDelay + "s")
top4  = menu.topElement("< Amm. Tyyppi  >", "STRING", "       v       ")
top5  = menu.topElement("<  LED-Ohjaus  >", "STRING", "    < OFF >    ")
top6  = menu.topElement("<  Aaniohjaus  >", "STRING", "    < OFF >    ") 

sub13 = menu.subElement("Wi-Fi Signal:   ", "BASH", "iwconfig wlan0 | awk -F'[ =]+' '/Signal level/ {print $7}' | cut -d/ -f1")
sub12 = menu.subElement("Wi-Fi SSID:     ", "BASH", "iwconfig wlan0 | grep 'ESSID:' | awk '{print $4}' | sed 's/ESSID://g'")
sub14 = menu.subElement("Internet:       ", "BASH", "ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error")
sub11 = menu.subElement("IP Address:     ", "BASH", "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1")
sub22 = menu.subElement("CPU-Load:       ", "PYTHON", 'str(str(psutil.cpu_percent()) + "%")')
sub23 = menu.subElement("CPU-Temp:       ", "BASH", "vcgencmd measure_temp | cut -c 6-15")
sub24 = menu.subElement("Memory:         ", "PYTHON", 'str(str(psutil.phymem_usage()[3])+"% used")')
sub31 = menu.subElement("Aika sekunteina:", "STRING", "30")
sub32 = menu.subElement("Aika sekunteina:", "STRING", "15")
sub33 = menu.subElement("Aika sekunteina:", "STRING", "0")
sub21 = menu.subElement("Datetime:       ", "PYTHON", "datetime.now().strftime('%b %d  %H:%M:%S')")
sub25 = menu.subElement("Python Version: ", "BASH", "python --version")
sub26 = menu.subElement("Foobar!         ", "PYTHON", "shoot.pythonTesti()")

# Add elements to the menu
# TODO: Iterator

menu.addTopElement(top1)
menu.addTopElement(top2)
menu.addTopElement(top3)
menu.addTopElement(top4)
menu.addTopElement(top5)
menu.addTopElement(top6)

menu.addSubElement(top1, sub11)
menu.addSubElement(top1, sub12)
menu.addSubElement(top1, sub13)
menu.addSubElement(top1, sub14)
menu.addSubElement(top2, sub21)
menu.addSubElement(top2, sub22)
menu.addSubElement(top2, sub23)
menu.addSubElement(top2, sub24)
menu.addSubElement(top3, sub31)
menu.addSubElement(top3, sub32)
menu.addSubElement(top3, sub33)
menu.addSubElement(top2, sub25)
menu.addSubElement(top2, sub26)

# Read Config
#load_config("mcshoot.cfg")

# Initialize the LCD display
lcd.clear()
lcd.begin(16,1)

# Unnecessary but professional looking loading display :)
i = 0
lcd.message("Initializing...\n")
while(i < 16):
    lcd.message(chr(255))
    sleep(.1)
    i += 1

# Start the menu
menu.startMenu(lcd)

