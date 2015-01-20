# McShoot

McShoot is a hobby project based around Raspberry Pi that allows you to do various timed scenarios for target shooting practising. The goal is to have a working prototype from which to iterate onwards.

### Info

There are two ways of using McShoot: with the Raspberry Pi hardware and LCD screen or in a simulated mode, which just runs the timer sequence and outputs to the screen. The latter one is used also with the real deal and is set by parameter. Simulation is used to make development easier without having to run all the changes in the real hardware.


### Usage

The timer flow goes as follows in the real hardware mode:

```sh
$ sudo ./mcsMenu.py
```
NOTE: Superuser privileges are needed to run the python to control the hardware

### User Interface

Interacting with the McShoot happens via the LCD shield. 

TODO: Screenshots and usage information

### Development / Simulator / Debugging

```sh
$ timer.py -o --output [lcd|screen] -c --color [true|false] -d --debug [true|false]
```

Parameters:

  - output: [ lcd | screen ] - print the progress to a lcd screen or stdout (default: screen)
  - color: [ true | false ] - use colored or monochrome output [Colorama] (default: true)
  - debug: [ true | false ] - print debug information to stdout while running (default: false)
  

### Flow
The timer flow in normal usage:

  1. Start
  2. Load
  3. Attention
  4. Shoot
  5. Stop
  6. Goto  3 if recursive mode set
  7. Unload


  
### Info

[ReadMe](README.md)

License
----
MIT


[Adafruit LCD shield]:https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/overview
[Adafruint LCD Library]:https://learn.adafruit.com/rgb-lcd-shield/using-the-rgb-lcd-shield
[Raspian]:http://www.raspian.org
[Python]:https://www.python.org
[Colorama]:https://pypi.python.org/pypi/colorama

