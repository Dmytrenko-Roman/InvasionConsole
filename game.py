from pynput import keyboard
import time
import os
import numpy as np

def draw(field, sx, sy, mx, my):
	result = ''

	for y, arr in enumerate(field):
		temp = ''
		for x, elem in enumerate(arr):
			if x == sx and y == sy:
				elem = 'o'
			if x == mx and y == my:
				elem = '|' 
			temp += str(elem)
		result += temp + '\n'

	return result


WIDTH = 8
HEIGHT = 10
shipX = WIDTH / 2
shipY = HEIGHT
missileX = shipX
missileY = shipY
MISSILE_DIR_Y = 1
DIFFICULTY = 0.4
ENEMIES_HEIGHT = [1, 4]
ENEMIES_WIDTH = [1, WIDTH]


top = ['╔', '╗']
bot = ['╚', '╝']
middle = ['║', '║']
field = []


for _ in range(WIDTH):
	top.insert(1, '═')
	bot.insert(1, '═')
	middle.insert(1, ' ')
	
for _ in range(HEIGHT):
	field.append(middle)

field.append(bot)
field.insert(0, top)

arr1 = [
	['╔', '═', '═', '═', '═', '═', '═', '═', '═', '╗'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],  
	['╚', '═', '═', '═', '═', '═', '═', '═', '═', '╝']
]

for y in range(ENEMIES_HEIGHT[0], ENEMIES_HEIGHT[1]):
	for x in range(ENEMIES_WIDTH[0], ENEMIES_WIDTH[1] + 1):
		arr1[y][x] = '-'


def press_instruction(key):
	pass


def release_instruction(key):
	pass


keyboard.Listener(
	on_press=press_instruction,
	on_release=release_instruction
).start()


while True:
	missileY -= MISSILE_DIR_Y
	y = round(missileY)
	x = round(missileX)
	if arr1[y][x] == '-' or arr1[y][x] == '═':
		arr1[y][x] = ' '
		missileY = shipY
		missileX = shipX
	
	os.system('cls')
	print(draw(arr1, shipX, shipY, missileX, missileY))
	time.sleep(DIFFICULTY)
