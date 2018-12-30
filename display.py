#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637

# Initialize the display (GND, VCC=3.3V, Example Pins are DIO-21 and CLK20)
Display = tm1637.TM1637(CLK=20, DIO=21, brightness=1.0)

# Display.ShowDoublepoint(True)
Display.SetBrightness(0.1)

itime = 1000
while True:
  digits=[int(tmp) for tmp in str(itime)]
  Display.Show(digits)
  sleep(.05)
  itime=itime+1

Display.cleanup()
