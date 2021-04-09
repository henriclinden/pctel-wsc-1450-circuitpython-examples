#
# ST LSM9DS1: 3-axis Magnetometer, 3-axis Accelerometer,
#             and 3-axis Gyroscope
#

import board
import digitalio
import busio
import time
import adafruit_lsm9ds1

# Ensure automatic deinit
with digitalio.DigitalInOut(board.SENSOR_POWER_ENABLE) as en:
    en.direction = digitalio.Direction.OUTPUT
    en.value = True
    time.sleep(0.1)  # Important: sleep to let power stabilize

    with busio.I2C(board.SCL, board.SDA) as i2c:
            lsm9ds1 = adafruit_lsm9ds1.LSM9DS1_I2C(i2c, mag_address=0x1c, xg_address=0x6a)

            while True:
                print("Temperature: %0.1f degC" % lsm9ds1.temperature)
                print("Gyro:         ", list(lsm9ds1.gyro))
                print("Magnetic:     ", list(lsm9ds1.magnetic))
                print("Acceleration: ", list(lsm9ds1.acceleration))
                time.sleep(1.0)