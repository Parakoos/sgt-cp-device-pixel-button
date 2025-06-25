import board

# ---------- LED Setup -------------#
# Currently, only NeoPixel LEDs are supported, but future versions might change this.
# Set the LED_PIN to None if you want to disable the light.
LED_PIN = board.P0_09
LED_COUNT = 32
LED_BRIGHTNESS = 0.75

# ---------- Bluetooth Setup -------------#
# Only the name of the Bluetooth device can be changed.
BLE_DEVICE_NAME = "Pixel Button"

# ---------- Button Setup -------------#
# Only a single button is supported here.
BTN_PIN = board.P1_06

# ---------- Timer Alert -------------#
# There are many options of what to do when a timer alert is triggered.
# This device configuration supports turning something on and off in a
# blinking fashion, but each device could have their own way to
# communicate an alert. Set up the on/off methods accpording to your board.
# Some examples are given below. Uncomment and edit as you see fit.

# Option 1: Nothing
def alert_on():
	pass
def alert_off():
	pass
# End Option 1

# Option 2: Vibrate a tiny motor by turning a pin on and off
# import digitalio
# VIBRATION_PIN = board.P1_04
# vibration = digitalio.DigitalInOut(VIBRATION_PIN)
# vibration.direction = digitalio.Direction.OUTPUT
# vibration.value = False
# def alert_on():
# 	vibration.value = True
# def alert_off():
# 	vibration.value = False
# End Option 2
