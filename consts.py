import board

USE_CONSOLE_INPUT = False

# ID pins
ID_PLUS_1_PIN = 10
ID_PLUS_2_PIN = 9
ID_RED_BLUE_PIN = 8

# basic LED settings
LED_SIG_PIN = board.D18
LED_NUMBER = 27
LED_INTERVAL_TIMEOUT = 0.07
BRIGHTNESS = 0.8

# LED colors
PRELIMINARY_COLOR = 0x640064 # Magenta
CONSOLE_COLOR = 0x646400 # Yellow
ERROR_COLOR = 0x640033
TEST_COLOR = 0x643300

RED_ALLIANCE_COLOR = 0xFF0000
BLUE_ALLIANCE_COLOR = 0x0000FF

RAINBOW_COLORS = [
    0x990000,
    0x999900,
    0x009900,
    0x009999,
    0x000099,
    0x990099
]

# Websocket
USE_WEBSOCKET = True
WS_URL = "http://127.0.0.1:3000"
WS_KEY = "fowlfield"
WS_TIMEOUT = 5000