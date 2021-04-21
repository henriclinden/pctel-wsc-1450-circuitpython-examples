#
# Using the Telit ME910C1 module to get the current position.
#

import time
import busio
import board
import digitalio


with digitalio.DigitalInOut(board.CELL_POWER_ENABLE) as en:
    en.switch_to_output(value=False)
    time.sleep(0.1)
    en.value = True
    time.sleep(0.1)

    on = digitalio.DigitalInOut(board.CELL_ON_OFF)
    on.switch_to_output(value=True)
    time.sleep(0.1)
    en.value = False
    time.sleep(5.0)
    en.value = True
    time.sleep(20.0)

    # The UART implementation do not have support for hardware flow control.
    rts = digitalio.DigitalInOut(board.CELL_RTS)
    rts.switch_to_output(value=False)
    cts = digitalio.DigitalInOut(board.CELL_CTS)
    cts.switch_to_input()

    uart = busio.UART(tx=board.CELL_TX, rx=board.CELL_RX, baudrate=115200, timeout=1)

    # Configure the modem to send NMEA data every second.
    commands = [b'AT$GPSP=1', b'AT$GPSNMUN=3,0,0,0,0,1,0']
    for command in commands:
        uart.write(command + b'\r')
        response = uart.readline()
        while not response.find(b'OK\r'):
            response = uart.readline()

    # Print navigation data.
    while True:
        print(uart.readline())




