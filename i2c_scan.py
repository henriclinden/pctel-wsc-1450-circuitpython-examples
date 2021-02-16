#
# Find all attached I2C devices
#

import board
import digitalio
import busio
import time

# Ensure automatic deinit
with digitalio.DigitalInOut(board.SENSOR_POWER_ENABLE) as en:
    en.direction = digitalio.Direction.OUTPUT
    en.value = True
    time.sleep(0.1) # Important: sleep to let power stabilize

    with busio.I2C(board.SCL, board.SDA) as i2c:
        i2c.try_lock()
        print(list(map(hex, i2c.scan())))
        i2c.unlock()
