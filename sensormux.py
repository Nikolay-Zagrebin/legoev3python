#!/usr/bin/env python3
from ev3dev2.port import LegoPort
from ev3dev2.led import Leds
from ev3dev2.sensor import Sensor
from TouchMuxed import TouchMuxed

"""
Example of using the TouchMuxed class
the address format is:

in[PORT]:i2c8[MUX port minus 1]:mux[MUX port]

so a sensor on the 2nd mux of port 3 is
in3:i2c81:mux2

"""

touch1 = TouchMuxed(address = "in1:i2c80:mux1")
touch2 = TouchMuxed(address = "in1:i2c81:mux2")

leds = Leds()

while True:
    if touch1.is_pressed:
        leds.set_color("LEFT", "GREEN")
    else:
        leds.set_color("LEFT", "RED")
    if touch2.is_pressed:
        leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("RIGHT", "RED")
