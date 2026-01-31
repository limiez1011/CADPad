import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler


keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP8, board.GP7, board.GP9, board.GP10)
keyboard.row_pins = (board.GP1, board.GP2, board.GP3)

keyboard.diode_orientation = DiodeOrientation.COL2ROW



encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP4, board.GP11, None, False),)
keyboard.modules.append(encoder_handler)

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP4, board.GP11, None, False),)

# SDA=GP5, SCL=GP6
try:
    import busio
    from adafruit_ssd1306 import SSD1306_I2C

    i2c = busio.I2C(board.GP6, board.GP5)
    display = SSD1306_I2C(128, 32, i2c)

    def oled_text(line1="", line2=""):
        try:
            display.fill(0)
            display.text(line1, 0, 0, 1)
            display.text(line2, 0, 12, 1)
            display.show()
        except Exception:
            pass

    oled_text("KMK ready", "")
except Exception:
    display = None
    def oled_text(*a, **k):
        return

# Encoder: CW = volume up, CCW = volume down, press = mute
def enc_cw(encoder, _):
    keyboard.tap_key(KC.AUDIO_VOL_UP)
    oled_text("Encoder:", "Vol Up")

def enc_ccw(encoder, _):
    keyboard.tap_key(KC.AUDIO_VOL_DOWN)
    oled_text("Encoder:", "Vol Down")

def enc_press(encoder, _):
    keyboard.tap_key(KC.MUTE)
    oled_text("Encoder:", "Mute")

encoder_handler.callbacks = ((enc_cw, enc_ccw, enc_press),)
keyboard.modules.append(encoder_handler)

keyboard.keymap = [
    [
        # Row 1
        KC.A, KC.B, KC.C, KC.D,
        # Row 2
        KC.E, KC.F, KC.G, KC.H,
        # Row 3
        KC.I, KC.J, KC.K, KC.L,
    ]
]


if __name__ == '__main__':
    keyboard.go()