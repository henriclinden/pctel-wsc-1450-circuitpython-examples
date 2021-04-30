#
# Modulating the onboard LED using VL53L0X Time-of-Flight [ToF] ranging sensor
#

import board
import digitalio
import busio
import time
import adafruit_vl53l0x

# Ensure automatic deinit
with digitalio.DigitalInOut(board.SENSOR_POWER_ENABLE) as en:
    en.direction = digitalio.Direction.OUTPUT
    en.value = True
    time.sleep(0.1)  # Important: sleep to let power stabilize

    with busio.I2C(board.SCL, board.SDA) as i2c:
        vl53 = adafruit_vl53l0x.VL53L0X(i2c, address=0x29)
        with digitalio.DigitalInOut(board.LED_RED) as led:
            led.switch_to_output(value=False)
            while True:
                #print("Range: {0}mm".format(vl53.range))
                time.sleep(vl53.range / 8000)
                led.value = not led.value


    


