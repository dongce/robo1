import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

gpio.setup(19, gpio.OUT)
gpio.setup(26, gpio.OUT)


def right_forward() :
    gpio.output(20, False)
    gpio.output(21, True)


def right_stop() :
    gpio.output(20, False)
    gpio.output(21, False)

def right_backward() :
    gpio.output(21, False)
    gpio.output(20, True)


def left_forward() :
    gpio.output(19, False)
    gpio.output(26, True)


def left_stop() :
    gpio.output(19, False)
    gpio.output(26, False)

def left_backward() :
    gpio.output(26, False)
    gpio.output(19, True)


def forward() :
    left_forward()
    right_forward()
    
def backward() :
    left_backward()
    right_backward()

def stop() :
    left_stop()
    right_stop()

    
def left() :
    left_stop()
    right_forward()

def right() :
    right_stop()
    left_forward()

