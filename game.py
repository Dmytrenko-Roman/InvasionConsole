from pynput import keyboard
import time
import os


def draw():
	field = [
		['╔', '═', '═', '═', '═', '═', '═', '═', '╗'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
		['╚', '═', '═', '═', '═', '═', '═', '═', '╝'],
		]
	return field


def press_instruction(key):
	pass


def release_instruction(key):
	pass


keyboard.Listener(
	on_press=press_instruction,
	on_release=release_instruction
).start()
