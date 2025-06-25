import adafruit_logging as logging
log = logging.getLogger()
log.setLevel(10)

from pixel_button.pixel_button_settings import BLE_DEVICE_NAME, BTN_PIN, LED_BRIGHTNESS, LED_COUNT, LED_PIN, alert_on, alert_off

# ---------- VIEW SETUP -------------#
from core.view.view_multi import ViewMulti
from core.view.view_console import ViewConsole
from pixel_button.view_mono_light import ViewMonoLight
from pixel_button.view_time_reminder_onoff import ViewTimeReminderOnOff
from pixel_button.pausable_pixels import PausablePixels
pixels = PausablePixels(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False)

view = ViewMulti([
	ViewConsole(),
	ViewMonoLight(pixels),
	ViewTimeReminderOnOff(alert_on, alert_off),
	])
view.set_state(None)

# ---------- BLUETOOTH SETUP -------------#
BLUETOOTH_FIELD_DIVIDER = ';'
BLUETOOTH_FIELD_ORDER = ['sgtTimerMode','sgtState','sgtColorHsv','sgtTurnTime','sgtPlayerTime','sgtTotalPlayTime','sgtTimeReminders']
from core.connection.sgt_connection_bluetooth import SgtConnectionBluetooth
sgt_connection = SgtConnectionBluetooth(view,
		device_name=BLE_DEVICE_NAME,
		field_order=BLUETOOTH_FIELD_ORDER,
		field_divider=BLUETOOTH_FIELD_DIVIDER,
	)

# ---------- BUTTONS SETUP -------------#
from core.buttons import Buttons
from microcontroller import Pin
buttons = Buttons({BTN_PIN: False})
def btn_callback(pin: Pin, presses: int, long_press: bool):
	log.info(f"Button pressed: {presses} times, long press: {long_press}")
	def on_success():
		pass

	if long_press:
		if presses == 1:
			sgt_connection.enqueue_send_toggle_admin(on_success=on_success)
		elif presses == 2:
			sgt_connection.enqueue_send_undo(on_success=on_success)
	else:
		if presses == 1:
			sgt_connection.enqueue_send_primary(on_success=on_success)
		elif presses == 2:
			sgt_connection.enqueue_send_secondary(on_success=on_success)

def pressed_keys_callback(pins: set[Pin]):
	if len(pins) == 0:
		pixels.pause = False
		pixels.fill(0x0)
		pixels.show()
	else:
		pixels.pause = False
		pixels.fill(0xFFFFFF)
		pixels.show()
		pixels.pause = True

# ---------- MAIN LOOP -------------#
from core.loop import main_loop, ErrorHandlerResumeOnButtonPress
error_handler = ErrorHandlerResumeOnButtonPress(view, buttons)
def on_connect():
	buttons.clear_callbacks()
	buttons.set_callback(pin=BTN_PIN, presses=1, callback = btn_callback)
	buttons.set_callback(pin=BTN_PIN, presses=2, callback = btn_callback)
	buttons.set_callback(pin=BTN_PIN, presses=1, long_press=True, callback = btn_callback)
	buttons.set_callback(pin=BTN_PIN, presses=2, long_press=True, callback = btn_callback)
	buttons.set_pressed_keys_update_callback(pressed_keys_callback)

main_loop(sgt_connection, view, on_connect, error_handler.on_error, (buttons.loop,))