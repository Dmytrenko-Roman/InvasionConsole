from pynput import keyboard
import time
import os


def draw(w, h):
	top = ['╔', '╗']
	bot = ['╚', '╝']
	middle = ['║', '║']
	field = []

	for _ in range(w):
		top.insert(1, '═')
		bot.insert(1, '═')
		middle.insert(1, ' ')
	
	for _ in range(h):
		field.append(middle)

	field.append(bot)
	field.insert(0, top)

	result = ''

	for y in field:
		temp = ''
		for x in y:
			temp += str(x)
		result += temp + '\n'

	return result


def press_instruction(key):
	pass


def release_instruction(key):
	pass


keyboard.Listener(
	on_press=press_instruction,
	on_release=release_instruction
).start()

print(draw(30, 10))
