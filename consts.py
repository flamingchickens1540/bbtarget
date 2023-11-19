import board

# basic LED settings
LED_SIG_PIN = board.D18
LED_NUMBER = 30
BRIGHTNESS = 0.5
LED_REFRESH_INTERVAL = 0.05

# LED colors
PRELIMINARY_COLOR = (255, 0, 255)
DEBUG_COLOR = (102, 51, 153)

RED_ALLIANCE_COLOR = (255, 0, 0)
BLUE_ALLIANCE_COLOR = (0, 0, 255)

FULL_BATTERY_COLOR = (0, 255, 0)
EMPTY_BATTERY_COLOR = (255, 0, 0)

# Websocket
USE_WEBSOCKET = True
WS_URL = "0.0.0.0"
WS_TIMEOUT = 5000