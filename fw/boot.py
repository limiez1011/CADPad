import storage
import board
import digitalio

# 1. Setup the Row (D0)
row = digitalio.DigitalInOut(board.D0)
row.direction = digitalio.Direction.INPUT
row.pull = digitalio.Pull.DOWN # Swapped from UP

# 2. Setup the Column (D9)
col = digitalio.DigitalInOut(board.D9)
col.direction = digitalio.Direction.OUTPUT
col.value = True # Swapped from False

# 3. The Logic
# If Row D0 is LOW (False), it means Key A is NOT pressed.
if not row.value:
    storage.disable_usb_drive()

# 4. Clean up
row.deinit()
col.deinit()
