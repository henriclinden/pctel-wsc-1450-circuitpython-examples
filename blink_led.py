#
# Blink red LED
#

import board
import digitalio
import time

with digitalio.DigitalInOut(board.LED_RED) as led:
    led.switch_to_output(value=False)
    while True:
        time.sleep(0.5)
        led.value = not led.value

