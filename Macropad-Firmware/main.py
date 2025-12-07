# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import press, Release, tap, Macros


# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)


# Define your pins here!
PINS = [board.D11, board.D10, board.D9, board.D8, board.D4, board.D3, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

copy = KC.MACRO(
    press(KC.LCTL),
    tap(KC.C),
    Release(KC.LCTL)
)

paste = KC.MACRO(
    press(KC.LCTL),
    tap(KC.V),
    Release(KC.LCTL)
)

switch = KC.MACRO(
    press(KC.LALT),
    tap(KC.tab),
    Release(KC.LALT)
)

open_tab = KC.MACRO(
    press(KC.LCTL),
    tap(KC.T),
    Release(KC.LCTL)
)

close_tab = KC.MACRO(
    press(KC.LCTL),
    tap(KC.w),
    Release(KC.LCTL)
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    copy, paste, switch, KC.F3, open_tab, close_tab, KC.PGUP, KC.PGDN
]
    

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
