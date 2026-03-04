import board
import busio
import adafruit_ssd1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D9, board.D8, board.D6, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D3, board.D10, None, False),)
encoder_handler.map = [((KC.UP, KC.DOWN, None),)]
keyboard.modules.append(encoder_handler)

try:
    i2c = busio.I2C(board.D5, board.D4)
    display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    display.fill(0)
    display.text('  CADPAD V1.8', 20, 4, 1)
    display.line(0, 16, 128, 16, 1)
    display.text('S:SRCH D:DIM E:EXT', 10, 20, 1)
    display.show()
except Exception as e:
    print(f"OLED Error: {e}")

keyboard.keymap = [[
    KC.MPRV,         KC.MPLY,         KC.MNXT,         KC.MUTE,          # Row 1
    KC.LALT(KC.TAB), KC.LCTRL(KC.C),  KC.LCTRL(KC.V),  KC.LCTRL(KC.Z),   # Row 2
    KC.S,            KC.D,            KC.E,            KC.L              # Row 3
]]

if __name__ == '__main__':
    keyboard.go()
