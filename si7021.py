#
# SI7021
#

import board
import digitalio
import busio
import time
import adafruit_si7021

# Ensure automatic deinit
with digitalio.DigitalInOut(board.SENSOR_POWER_ENABLE) as en:
    en.direction = digitalio.Direction.OUTPUT
    en.value = True
    time.sleep(0.1)  # Important: sleep to let power stabilize

    with busio.I2C(board.SCL, board.SDA) as i2c:
            si7021 = adafruit_si7021.SI7021(i2c, address=0x40)

            while True:
                print("Temperature: %0.1f degC" % si7021.temperature)
                print("Humidity   : %0.1f %%" % si7021.relative_humidity)
                time.sleep(2)