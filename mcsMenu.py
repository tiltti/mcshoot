# Using Menu.py made by Daniel Juenger (github.com/sleeepyjack)
# Using Adafruit_CharLCDPlate library by Adafruit Industries (github.com/adafruit)

# dependencies: Colorama

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from menu import Menu
from subprocess import *
from time import sleep, strftime

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

# The menu can show strings, bash and python expressions
#
#           topElement(      Top row Name, Type    , Low row content)
top1 = menu.topElement("< 1. Network   >", "STRING", "        v")
top2 = menu.topElement("< 2. System    >", "STRING", "        v")
top3 = menu.topElement("< 3. McShoot   >", "STRING", "        v")
top4 = menu.topElement("< 4. NotUsed   >", "STRING", "         ")
top5 = menu.topElement("< 5. NotUsed   >", "STRING", "         ")
sub13 = menu.subElement("1 > Signal      ", "BASH", "iwconfig wlan0 | awk -F'[ =]+' '/Signal level/ {print $7}' | cut -d/ -f1")
sub12 = menu.subElement("1 > SSID        ", "BASH", "iwconfig wlan0 | grep 'ESSID:' | awk '{print $4}' | sed 's/ESSID://g'")
sub14 = menu.subElement("1 > Internet    ", "BASH", "ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error")
sub11 = menu.subElement("1 > IP Address  ", "BASH", "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1")
sub22 = menu.subElement("2 > CPU-Load    ", "PYTHON", 'str(str(psutil.cpu_percent()) + "%")')
sub23 = menu.subElement("2 > CPU-Temp    ", "BASH", "vcgencmd measure_temp | cut -c 6-15")
sub24 = menu.subElement("2 > Memory      ", "PYTHON", 'str(str(psutil.phymem_usage()[3])+"% used")')
sub21 = menu.subElement("2 > Datetime ", "PYTHON", "datetime.now().strftime('%b %d  %H:%M:%S')")

# Add elements to the menu
# TODO: Iterator

menu.addTopElement(top1)
menu.addTopElement(top2)
menu.addTopElement(top3)
menu.addTopElement(top4)
menu.addTopElement(top5)

menu.addSubElement(top1, sub11)
menu.addSubElement(top1, sub12)
menu.addSubElement(top1, sub13)
menu.addSubElement(top1, sub14)
menu.addSubElement(top2, sub21)
menu.addSubElement(top2, sub22)
menu.addSubElement(top2, sub23)
menu.addSubElement(top2, sub24)

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

