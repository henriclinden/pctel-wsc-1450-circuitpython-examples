#
# BME680 Environmental Gas / Air Quality + temperature and humidity
#

import board
import digitalio
import busio
import time
import adafruit_bme680

# Ensure automatic deinit
with digitalio.DigitalInOut(board.SENSOR_POWER_ENABLE) as en:
    en.direction = digitalio.Direction.OUTPUT
    en.value = True
    time.sleep(0.1)  # Important: sleep to let power stabilize

    with busio.I2C(board.SCL, board.SDA) as i2c:
            bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x76)
            bme680.sea_level_pressure = 1013.25  # sea level pressure in hPa

            while True:
                print("Temperature: %0.1f degC" % bme680.temperature)
                print("Gas: %d ohm" % bme680.gas)
                print("Humidity: %0.1f %%" % bme680.relative_humidity)
                print("Pressure: %0.3f hPa" % bme680.pressure)
                print("Altitude = %0.2f meters" % bme680.altitude)
                time.sleep(2)
