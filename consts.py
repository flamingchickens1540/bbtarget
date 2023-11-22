import board

# basic LED settings
LED_SIG_PIN = board.D18
LED_NUMBER = 27
LED_INTERVAL_TIMEOUT = 0.05
BRIGHTNESS = 0.8

# LED colors
PRELIMINARY_COLOR = 0x640064 # Magenta
DEBUG_COLOR = 0x646400 # Yellow

RED_ALLIANCE_COLOR = 0xFF0000
BLUE_ALLIANCE_COLOR = 0x0000FF

# Websocket
USE_WEBSOCKET = True
WS_URL = "http://127.0.0.1:3000"
WS_KEY = "fowlfield"
WS_TIMEOUT = 5000