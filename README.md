# pctel-wsc-1450-circuitpython-examples

CircuitPython examples for PCTEL WSC-1450 and WSDK-1450.

1. The CircuitPython lib needs to be installed to run the examples. Download the library pack from CircuitPython website: https://circuitpython.org/libraries
2. Details and tutorials on how to use CircuitPython in general, and the Adafruit libraries in particular, can be found here: https://learn.adafruit.com/welcome-to-circuitpython

Download, extract, and copy the /lib directory to WSC-1450, connect a serial console to "Target USB" @ 115200,8,n,1, press Ctrl-d to soft reset the ASC-1450, and press a key to get the REPL started!

Happy hacking!



# How to run the examples

The examples are run via Python's import statement. The WSC-1450 needs to be soft reset (using Ctrl-d) before the import statment is run.

![How to run an example](https://github.com/henriclinden/pctel-wsc-1450-circuitpython-examples/blob/main/doc/bme640.png)

# Simple Bluetooth Low Energy example

![Simple BLE scan example](https://github.com/henriclinden/pctel-wsc-1450-circuitpython-examples/blob/main/doc/ble_scan.png)
