from serial import Serial
import struct
import domain.st10.monitor_comm as comm
from domain.mcu_addressing import MCULogicalAddressRange
from domain.st10.st10f276 import ST10F276FlashBlocksCatalog
from intelhex import IntelHex

p = Serial('/dev/ttyS0', 9600)
def accept_chip_id(chip_id):
     print("CHIP ID: " + str(chip_id))
     return True

startchipid_hex_filename='startchipid.hex'
monitor_hex_filename='Monitor004b.hex'
comm.MonitorRemoteLauncher(device=p, startchipid_hex_filename=startchipid_hex_filename, monitor_hex_filename=monitor_hex_filename, validate_chip_id=accept_chip_id).start()