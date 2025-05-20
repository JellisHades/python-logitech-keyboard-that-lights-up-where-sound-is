from logiled import LogitechLed, load_dll
from pynput import keyboard
import threading
import time
load_dll()

led = LogitechLed()

Zones = {
	1: [
		'esc', "f1", "f2", "f3",
		"`", "~", "1", "!", "2", "@", "3", "#", "4", "$",
		"tab", "q", "Q", "w", "W", "e", "E", "r", "R",
		"caps_lock", "a", "A", "s", "S", "d", "D", "f", "F",
		"shift", "z", "Z", "x", "X", "c", "C",
		"ctrl_l", "cmd", "alt_l"
	],
	
	2: [
		'f4', "f5", "f6", "f7", "f8",
		"5", "%", "6", "^", "7", "&", "8", "*", "9", "(",
		"t", "T", "y", "Y", "u", "U", "i", "I",
		"g", "G", "h", "H", "j", "J", "k", "K",
		"v", "V", "b", "B", "n", "N", "m", "M",
		"space",
	],
	
	3: [
		'f9', "f10", "f11", "f12",
		"0", ")", "-", "_", "=", "+", "backspace",
		"o", "O", "p", "P", "[", "{", "]", "}", "\\", "|",
		"l", "L", ";", ":", '"', "'", "enter",
		"<", ",", ".", ">", "/", "?", "shift_r",
		"alt_gr", "cmd_r", "menu", "ctrl_r"
	],

	4: [
		'print_screen', "scroll_lock", "pause",
		"insert", "home", "page_up",
		"delete", "end", "page_down",
		"up",
		"left", "down", "right"
	],
}

FlashingZones = {}

def FlashZone(Zone):
	if Zone in FlashingZones and FlashingZones[Zone] > 0:
		FlashingZones[Zone] = 100
		return
	
	FlashingZones[Zone] = 100

	while FlashingZones[Zone] > 0:
		led.set_lighting_for_target_zone(Zone, 0, 0, FlashingZones[Zone])
		FlashingZones[Zone] -= 10
		time.sleep(0.1)

def on_press(PressedKey):
	KeyName = None

	try:
		KeyName = PressedKey.char 
	except:
		KeyName = PressedKey.name
	
	for TargetZone in Zones:
		for Key in Zones[TargetZone]:
			if Key != KeyName:
				continue
			
			threading.Thread(target=FlashZone, args=(TargetZone,)).start()
			break

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()