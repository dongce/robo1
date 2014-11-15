import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.OUT)
gpio.output(20, False)
gpio.setup(21, gpio.OUT)
gpio.output(21, True)
