#!/usr/bin/env python3

from ev3dev2.motor import Motor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor import INPUT_2, INPUT_3

motor1 = Motor(address = 'in1:i2c3:M1')
motor2 = Motor(address = 'in1:i2c3:M2')

touch1 = TouchSensor(INPUT_2)
touch2 = TouchSensor(INPUT_3)

motor1.speed_sp = 200
motor2.speed_sp = 200

#these motor instructions aren't very good
# don't use them as an example of proper motor control

while True:
	if touch1.is_pressed:
		motor1.position_sp = 100
	else:
		motor1.position_sp = 0

	if touch2.is_pressed:
		motor2.position_sp = 360
	else:
		motor2.position_sp = 180

	motor1.run_to_abs_pos()
	motor2.run_to_abs_pos()
