# CircuitPython for WSC-1450

## Install

1.  Connect the DHD USB debug port to your PC using a USB cable. Make sure the Target Power strap is put to enable power from USB port. This will present a new attached storage called "DAPLINK:".
1.  Copy nRF52 SoftDevice binary (s140_nrf52_6.1.0_softdevice.hex) to DAPLINK:
1.  Let the device restart.
1.  Copy CircuitPython binary (pctel_wsc_1450_YYYY.MM.DD_firmware.hex) to DAPLINK:
1.  Let the device restart.
1.  Connect a USB port to "Target USB". A new disk will appear "CIRCUITPY:". This disk is the flash memory of WSDK-1450. 
1.  Follow instructions on CircuitPython website to install libraries to flash memory. Firmware 02.12 uses 6.x libraries and 05.28 uses 7.x.

Have fun!

NOTE: If the firmware do not seem to work, or if there is no "CIRCUITPY:" drive detected when plugging in the USB, then the flash memory probably not correctly initialized and needs to be erased completly before programming the softdevice and firmware. This can be done using the pyOCD software kit. See the pyOCD Programming section below and https://pyocd.io/ for details.

## Ref

Source code for the firmware above are in this repo: [henriclinden/circuitpython](https://github.com/henriclinden/circuitpython). Use the branch "pctel_wsc_1450"

## pyOCD Programming

If the unit have not before been programmed with circuitpython, or if the softdevice needs to be updated, flash memory needs to be erased. This is acompliced using the “erase” subcommand of pyOCD.

```
pyocd erase
```

After erase is completed, softdevice and firmware can be programmed. 

```
pyocd load s140_nrf52_6.1.0_softdevice.hex

pyocd load pctel_wsc_1450_2021.05.28_firmware.hex
```

To start the newly installed firmware, issue a reset.

```
pyocd reset
```
