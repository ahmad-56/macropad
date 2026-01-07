import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rotary_encoder import RotaryEncoder
from kmk.modules.rgb import RGB
from kmk.extensions.display import OLED

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)   # Example: 3 columns
keyboard.row_pins = (board.GP4, board.GP2, board.GP1)   # Example: 3 rows
keyboard.diode_orientation = "COL2ROW"                 # Adjust if needed

keyboard.keymap = [
    [
        KC.DEL, KC.PRINT_SCREEN, KC.NO,  # Row 0
        KC.LGUI, KC.UP, KC.KC.with_mods(KC.V, KC.MOD_LGUI), #WIN+V    # Row 1
        KC.LEFT, KC.DOWN, KC.RIGHT     # Row 2
    ]
]

encoder = RotaryEncoder(
    encoder_pins=(board.GP29, board.GP3),
    ccw=KC.VOLD,                          
    cw=KC.VOLU,                           
    button=KC.MUTE
)
keyboard.extended = [encoder]

keyboard.modules.append(
    RGB(
        pin=board.GP0,
        num_leds=8,
        brightness=0.4,
        auto_write=True
    )
)

from kmk.extensions.display import OLED

i2c = board.I2C(scl=board.GP7, sda=board.GP6)

keyboard.extensions.append(
    OLED(
        width=128,
        height=32,
        i2c_bus=i2c,
        flip=False,
        scroll=False
    )
)


keyboard.debug_enabled = True

if __name__ == "__main__":
    keyboard.go()