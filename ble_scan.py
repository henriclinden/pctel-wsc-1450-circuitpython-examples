#
# BLE scan
#

from adafruit_ble import BLERadio

ble = BLERadio()
found = set()
scan_responses = set()
for advertisement in ble.start_scan(timeout=10):
    addr = advertisement.address
    if advertisement.scan_response and addr not in scan_responses:
        scan_responses.add(addr)
    elif not advertisement.scan_response and addr not in found:
        found.add(addr)
    else:
        continue
    print(addr, advertisement)
    print("\t" + repr(advertisement))
    print()
