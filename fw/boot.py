import storage
import board
import digitalio

row = digitalio.DigitalInOut(board.D0)
row.direction = digitalio.Direction.INPUT
row.pull = digitalio.Pull.DOWN # Swapped from UP

col = digitalio.DigitalInOut(board.D9)
col.direction = digitalio.Direction.OUTPUT
col.value = True # Swapped from False

if not row.value:
    storage.disable_usb_drive()

row.deinit()
col.deinit()
