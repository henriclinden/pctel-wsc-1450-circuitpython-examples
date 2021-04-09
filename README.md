# pctel-wsc-1450-circuitpython-examples

CircuitPython examples for PCTEL WSC-1450 and WSDK-1450.

1. The CircuitPython lib needs to be installed to run the examples. Download the library pack from CircuitPython website: https://circuitpython.org/libraries
2. Details and tutorials on how to use CircuitPython in general, and the Adafruit libraries in particular, can be found here: https://learn.adafruit.com/welcome-to-circuitpython

Download, extract, and copy the /lib directory to WSC-1450, connect a serial console to "Target USB" @ 115200,8,n,1, press Ctrl-d to soft reset the ASC-1450, and press a key to get the REPL started!

Happy hacking!



# How to run the examples

The examples are run via Python's import statement. The WSC-1450 needs to be soft reset (using Ctrl-d) before the import statment is run.

Below shows how to test the Bosch BME680 gas sensor. This sensor measure relative humidity, barometric pressure, ambient temperature and gas. 

```python
Adafruit CircuitPython 6.2.0-beta.0-6-geb845ce16-dirty on 2021-02-12; WSC-1450 with nRF52840
>>> import bme680
Temperature: 26.2 degC
Gas: 414785 ohm
Humidity: 24.6 %
Pressure: 1005.335 hPa
Altitude = 66.11 meters
Temperature: 26.2 degC
Gas: 6218 ohm
Humidity: 24.6 %
Pressure: 1005.329 hPa
Altitude = 66.16 meters
```

# Simple Bluetooth Low Energy example

Here is an example of how to how to scan for Bluetooth Low Energy peripherals using the REPL.

```python
Adafruit CircuitPython 6.2.0-beta.0-6-geb845ce16-dirty on 2021-02-12; WSC-1450 with nRF52840
>>> from adafruit_ble import BLERadio
>>> radio = BLERadio()
>>> set(device.address for device in radio.start_scan(timeout=2, minimum_rssi=-80))

{<Address 6f:b9:ea:cc:7d:f0>, <Address 67:9e:25:cd:e7:f4>, <Address 42:7d:2e:d4:12:22>, <Address 84:c0:ef:d9:e5:46>, <Address 35:33:5b:a1:2a:85>, <Address 68:35:52:23:1b:9d>, <Address 42:05:e6:95:fd:cc>, <Address 9c:20:7b:ed:eb:dc>, <Address 39:d0:61:5d:dd:77>}
```
