import CHIP_IO.GPIO as GPIO
import time


# --- leds --- #

def led_init():
    GPIO.setup("XIO-P0", GPIO.OUT)
    GPIO.setup("XIO-P2", GPIO.OUT)
    GPIO.setup("XIO-P4", GPIO.OUT)
    GPIO.output("XIO-P0", GPIO.LOW)
    GPIO.output("XIO-P2", GPIO.LOW)
    GPIO.output("XIO-P4", GPIO.LOW)

def __led(led, state):
    # state
    if state == "off":
        state = GPIO.LOW
    elif state == "on":
        state = GPIO.HIGH
    else:
        return False
    # led
    if led == "green":
        led = "XIO-P0"
    elif led == "yellow":
        led = "XIO-P2"
    elif led == "orange":
        led = "XIO-P4"
    else:
        return False
    # execute
    return GPIO.output(led, state)

def led_off(led):
    return __led(led, "off")

def led_on(led):
    return __led(led, "on")


# --- buttons --- #

def button_init():
    GPIO.setup("XIO-P6", GPIO.IN)
    GPIO.setup("XIO-P7", GPIO.IN)

def button(button):
    if button == "one":
        button = "XIO-P6"
    elif button == "two":
        button = "XIO-P7"
    else:
        return False
    return GPIO.input(button)


# --- main test cyclle --- #

for i in range(3):
    led_on("green")
    time.sleep(1)
    led_on("yellow")
    time.sleep(1)
    led_on("orange")
    time.sleep(1)
    led_off("green")
    time.sleep(1)
    led_off("yellow")
    time.sleep(1)
    led_off("orange")
    time.sleep(1)

led_off("green")
led_off("yellow")
led_off("orange")

while True:
    if button("one"):
        led_on("green")
    else:
        led_off("green")

    if button("two"):
        led_on("yellow")
    else:
        led_off("yellow")

    time.sleep(0.25)


GPIO.cleanup()
