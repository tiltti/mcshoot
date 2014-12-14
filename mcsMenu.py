# Using Menu.py made by Daniel Juenger (github.com/sleeepyjack)
# Using Adafruit_CharLCDPlate library by Adafruit Industries (github.com/adafruit)

# dependencies: Colorama

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from menu import Menu
from subprocess import *
from time import sleep, strftime
#from timer import ShootUtils

# Utility function for runnin shell commands
def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
	return output

# Check the IP address 
#        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
#        lcd.message('IP %s' % ( ipaddr ) )

lcd = Adafruit_CharLCDPlate()
menu = Menu()
#shoot = ShootUtils()

# The menu can show strings, bash and python expressions
#
#           topElement(      Top row Name, Type    , Low row content
#                           max 16 chars
#                       <-------x-------->            <-------x------->
top1  = menu.topElement("<   Network    >", "STRING", "       v       ")
top2  = menu.topElement("<   System     >", "STRING", "       v       ")
top3  = menu.topElement("<   Alkuviive  >", "STRING", "       v       ")
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
sub31 = menu.subElement("Aika (s):       ", "STRING", "10")
sub32 = menu.subElement("Aika (s):       ", "STRING", "3")
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
menu.addSubElement(top2, sub25)
menu.addSubElement(top2, sub26)

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

