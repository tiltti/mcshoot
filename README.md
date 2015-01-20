# McShoot

McShoot is a hobby project based around Raspberry Pi that allows you to do various timed scenarios for target shooting practising. The goal is to have a working prototype from which to iterate onwards.

### MVP

Functionality for minimum viable product are:

  - Able to select from various pre-set timed scenarios
  - Start/stop/reset timers
  - Output status to a LCD screen, LED lights display and through audio

Further improvements that have been suggested:

  - Able to detetect when shots are being fired and store the timestamp
  - Allow adding custom timers/scenarios
  - Gather statistics and show them in the LCD display
  - External LED light support
  - etc.
 
## Tech

### Hardware

  - McShoot is built on top of Raspberry Pi and [Adafruit LCD shield]
  - Audio is using Raspberry Pi's built-in audio.
  - External communication is done via GPIO pins with 3.3V output as required (under construction).

### Sofware

  - Base installation is done on top of [Raspian] Linux OS

McShoot uses a lot of opensource goodies such as:

* [Python] - Python programming language
* [Adafruint LCD Library]
* [Colorama] for beautiful output 
* TODO: rest of the dependencies

### Installation

TODO

```sh
$ brew install ...
$ pip install ...
```

### Documentation

[Documentation](mcshoot.md)

### Development

Want to contribute? Great! Contact me first to get on board or feel free to suggest ideas :)

License
----

MIT


**Free Software, Hell Yeah!**

[Adafruit LCD shield]:https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/overview
[Adafruint LCD Library]:https://learn.adafruit.com/rgb-lcd-shield/using-the-rgb-lcd-shield
[Raspian]:http://www.raspian.org
[Python]:https://www.python.org
[Colorama]:https://pypi.python.org/pypi/colorama

