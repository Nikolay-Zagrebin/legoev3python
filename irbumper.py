#!/usr/bin/env python3
from ev3dev2.port import LegoPort
from ev3dev2.sensor import Sensor
from ev3dev2.sensor.lego import InfraredSensor
from MuxedSensors import TouchMuxed
from ev3dev2.motor import Motor, MoveTank, SpeedPercent, OUTPUT_B, OUTPUT_D

middle = TouchMuxed(address = "in1:i2c80:mux1")
right = TouchMuxed(address = "in1:i2c81:mux2")
left = TouchMuxed(address = "in1:i2c82:mux3")

ir = InfraredSensor()

tank = MoveTank(OUTPUT_B, OUTPUT_D)

current_speed = -100

def go_forward():
	tank.on(current_speed, current_speed)

def back_up():
	tank.on_for_seconds(100, 100, 2)

def rotate_left():
	tank.on_for_rotations(70, -70, 0.5)

def rotate_right():
	tank.on_for_rotations(-70, 70, 0.5)



while True:
	if ir.proximity < 90:
		current_speed = min(-30, -1 * ir.proximity)
	else:
		current_speed = -100

	if middle.is_pressed:
		back_up()
		rotate_left()
		rotate_left()
		continue
	if left.is_pressed:
		back_up()
		rotate_right()
		continue
	if right.is_pressed:
		back_up()
		rotate_left()
		continue
	
	go_forward()

