# Using Menu.py made by Daniel Juenger (github.com/sleeepyjack)
# Using Adafruit_CharLCDPlate library by Adafruit Industries (github.com/adafruit)

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from menu import Menu

from subprocess import *
from time import sleep, strftime
from datetime import datetime

cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"


#def run_cmd(cmd):
#        p = Popen(cmd, shell=True, stdout=PIPE)
#        output = p.communicate()[0]
#        return output
#
#while 1:
#        lcd.clear()
#        ipaddr = run_cmd(cmd)
#        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
#        lcd.message('IP %s' % ( ipaddr ) )
#        sleep(2)


lcd = Adafruit_CharLCDPlate()
menu = Menu()

# The menu can show strings, bash and python expressions
#
#           topElement(      Top row Name, Type    , Low row content)
top1 = menu.topElement("< 1. Network   >", "STRING", "        v")
top2 = menu.topElement("< 2. System    >", "STRING", "        v")
top3 = menu.topElement("< 3. McShoot   >", "STRING", "        v")
top4 = menu.topElement("< 4. NotUsed   >", "STRING", "        v")
top5 = menu.topElement("< 5. NotUsed   >", "STRING", "        v")
sub11 = menu.subElement("1 > Signal      ", "BASH", "iwconfig wlan0 | awk -F'[ =]+' '/Signal level/ {print $7}' | cut -d/ -f1")
sub12 = menu.subElement("1 > SSID        ", "BASH", "iwconfig wlan0 | grep 'ESSID:' | awk '{print $4}' | sed 's/ESSID://g'")
sub13 = menu.subElement("1 > Internet    ", "BASH", "ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo ok || echo error")
sub21 = menu.subElement("2 > CPU         ", "PYTHON", 'str(str(psutil.cpu_percent()) + "%")')
sub22 = menu.subElement("2 > CPU-Temp    ", "STRING", "TODO")
sub23 = menu.subElement("2 > Memory      ", "PYTHON", 'str(str(psutil.phymem_usage()[3])+"% used")')

#Adding elements to the menu
menu.addTopElement(top1)
menu.addTopElement(top2)
menu.addTopElement(top3)
menu.addTopElement(top4)
menu.addTopElement(top5)

menu.addSubElement(top1, sub11)
menu.addSubElement(top1, sub12)
menu.addSubElement(top1, sub13)
menu.addSubElement(top2, sub21)
menu.addSubElement(top2, sub22)
menu.addSubElement(top2, sub23)

#color = lcd.TEAL

#initializing display
lcd.clear()
lcd.begin(16,1)
#lcd.backlight(color)

#little loading animation
i = 0
lcd.message("LOADING...\n")
while(i < 16):
    lcd.message(chr(219))
    sleep(.1)
    i += 1

#starting the menu
menu.startMenu(lcd)

