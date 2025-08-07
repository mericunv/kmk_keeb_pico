import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC





keyboard = KMKKeyboard()




keyboard.debug_enabled = True
print("KMK is running")

# Define 16 rows (GP0 - GP15)
keyboard.row_pins = (
    board.GP12,  board.GP11,  board.GP15,  board.GP13,
    board.GP14,  board.GP10,  board.GP9,  board.GP8,
    board.GP7,  board.GP6,  board.GP5, board.GP4,
    board.GP3, board.GP2, board.GP1, board.GP0,
)

# Define 5 columns (GP16 - GP20)
keyboard.col_pins = (
    board.GP17, board.GP16, board.GP18, board.GP19, board.GP20
)

# Set diode orientation according to your wiring
keyboard.diode_orientation = DiodeOrientation.ROW2COL


keyboard.keymap = [
    [  # LAYER 0 (Base QWERTY)
        KC.NO,   KC.NO,    KC.NO,    KC.NO,    KC.NO,   
        KC.ESC,  KC.TAB,   KC.CAPS,  KC.LSFT,  KC.LCTL,
        KC.N1,   KC.Q,     KC.A,     KC.Z,     KC.LGUI,
        KC.N2,   KC.W,     KC.S,     KC.X,     KC.LALT,
        KC.N3,   KC.E,     KC.D,     KC.C,     KC.NO,
        KC.N4,   KC.R,     KC.F,     KC.V,     KC.NO,
        KC.N5,   KC.T,     KC.G,     KC.B,     KC.SPC,
        KC.N6,   KC.Y,     KC.H,     KC.N,     KC.NO,
        KC.N7,   KC.U,     KC.J,     KC.M,     KC.NO,
        KC.N8,   KC.I,     KC.K,     KC.COMM,  KC.RALT,
        KC.N9,   KC.O,     KC.L,     KC.DOT,   KC.RGUI,
        KC.N0,   KC.P,     KC.SCLN,  KC.SLSH,  KC.NO,
        KC.MINS, KC.LBRC,  KC.QUOT,  KC.RSFT,  KC.LEFT,
        KC.EQL,  KC.RBRC,  KC.ENT,   KC.UP,    KC.DOWN,
        KC.BSPC, KC.BSLS,  KC.NO,    KC.NO,    KC.NO,
        KC.PSCR, KC.DEL,   KC.NO,    KC.NO,    KC.RGHT, 
        
    ],

    [  # LAYER 1 (Fn Layer)
        KC.GRV, KC.NO,   KC.NO, KC.NO, KC.NO, 
        KC.F1,  KC.CAPS, KC.NO, KC.NO, KC.NO, 
        KC.F2,  KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F3,  KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F4,  KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F5,  KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F6,  KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F7,  KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F8,  KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F9,  KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F10, KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F11, KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.F12, KC.NO,   KC.NO, KC.NO, KC.NO,  
        KC.NO,  KC.NO,   KC.NO, KC.NO, KC.NO, 
        KC.NO,  KC.NO,   KC.NO, KC.NO, KC.NO, 
        KC.NO,  KC.NO,   KC.NO, KC.NO, KC.NO, 
    ]
]

if __name__ == '__main__':
    keyboard.go()
