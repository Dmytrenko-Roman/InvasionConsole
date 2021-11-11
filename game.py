from pynput import keyboard
import time
import os


def draw(field, sx, sy, mx, my):

	result = ''

	for y, arr in enumerate(field):
		temp = ''
		for x, elem in enumerate(arr):
			if x == sx and y == sy:
				elem = '^'
			if x == mx and y == my:
				elem = '×' 
			temp += str(elem)
		result += temp + '\n'

	return result


field = [
	['╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗'], 
	['║', '■', '■', '■', ' ', ' ', ' ', '■', '■', '■', '■', ' ', ' ', ' ', '■', '■', '■', '║'], 
	['║', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '║'], 
	['║', ' ', ' ', ' ', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', '■', '■', '■', '■', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
	['║', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', '║'], 
	['║', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', '║'], 
	['║', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'], 
	['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],  
	['╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝']
]


WIDTH = len(field[0]) - 2
HEIGHT = len(field) - 2
shipX = WIDTH / 2
shipY = HEIGHT
missileX = shipX
missileY = shipY - 1
MISSILE_DIR_Y = 1
DIFFICULTY = 0.1
BORDERS = [1, WIDTH]
winCondition = [0, 1, 2, 4, 5, 6, 7]


def press_instruction(key):
	global shipX, BORDERS
	if key == keyboard.KeyCode.from_char('a'):
		if shipX > BORDERS[0]:
			shipX -= 1
	elif key == keyboard.KeyCode.from_char('d'):
		if shipX < BORDERS[1]:
			shipX += 1


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
	isOver = True

	if field[y][x] == '■':
		field[y][x] = ' '
		missileY = shipY - 1
		missileX = shipX
	elif field[y][x] == '═':
		missileY = shipY - 1
		missileX = shipX
	
	for elem in winCondition:
		for arr in field[elem]:
				if '■' in arr:
					isOver = False 

	if isOver:
		print('You win!')
		break

	os.system('cls')
	print(draw(field, shipX, shipY, missileX, missileY))
	time.sleep(DIFFICULTY)
