import moveDrop
import utils


# Смена шапки
def harvestDinosaur():
	change_hat(Hats.Cactus_Hat)
	change_hat(Hats.Dinosaur_Hat)

# старт
def run():
	harvestDinosaur()
	clear()
	moveDrop.movePosition(0,0)
	count = {"value": 0}
	harvestDinosaur()
	while True:
		if count["value"] >= 30:
			print("start")
			allWord()
		else:
			moveDinosaur(count)



# идти к яблоку
def moveDinosaur(count):
	next_x, next_y = measure()
	if movePositionDinosaur(next_x, next_y) == False:
		harvestDinosaur()
		count["value"] = 0
		return
	count["value"] = count["value"]  + 1
	
# Обходить весь мир
def allWord():
	movePositionDinosaur(0,0)
	movePos = None
	x = get_pos_x()
	y = get_pos_y()

	if x == 0 and y == 0:
		movePos = "y"
	if x == get_world_size() - 1 and y == get_world_size() - 1:
		movePos = "x"

	if  movePos == "y":
		if y == get_world_size() - 1 or (y == 0 and x != 0):
			moveDroneNotCheck(East)
			x = get_pos_x()
		
		if x % 2 != 0:
			moveDroneNotCheck(South)
		if x % 2 == 0:
			moveDroneNotCheck(North)

	if  movePos == "x":
		if x == get_world_size() - 1 or (x == 0 and y != 0):
			moveDroneNotCheck(North)
			y = get_pos_y()
		
		if y % 2 != 0:
			moveDroneNotCheck(East)
		if y % 2 == 0:
			moveDroneNotCheck(West)

# Определеить позицию перемещения
def movePositionDinosaur(x,y):
	while True:
		xDrop = get_pos_x()
		yDrop = get_pos_y()

		if x > xDrop:
			if(moveDrone(East) == False):
				return False
			continue

		if x < xDrop:
			if(moveDrone(West) == False):
				return False
			continue

		if y > yDrop:
			if(moveDrone(North) == False):
				return False
			continue

		if y < yDrop:
			if(moveDrone(South) == False):
				return False
			continue

		if y == yDrop and x == xDrop:
			return True

# Переместить дрона
def moveDroneNotCheck(direction):
	if can_move(direction) == False:
		return False
	move(direction)

# Переместить дрона с проверками
def moveDrone(direction):
	listMove = []
	# Приоритетнее двигаться сюда
	isPath = False
	if can_move(direction):
		isPath = True
		
	# Проверка всех путей
	for itemDirection in utils.listDirection:
			if can_move(itemDirection):
				listMove.append(itemDirection)

	# Двигаюсь по приоритету
	if isPath == True:
		move(direction)
		return True

	# Пытаюсь спасти ситуацию
	if len(listMove) != 0:
		move(listMove[0])
	
	else:
		return False