import utils

def harvestDinosaur(count):
	change_hat(Hats.Cactus_Hat)
	count["value"] =  0
	change_hat(Hats.Dinosaur_Hat)

def run():
	change_hat(Hats.Cactus_Hat)
	clear()
	harvest()
	count = {"value": 0}
	preMove = {"x": None, "y": None}
	change_hat(Hats.Dinosaur_Hat)
	while True:
		next_x, next_y = measure()
		if movePositionDinosaur(next_x, next_y, preMove) == False:
			harvestDinosaur(count)
			continue
		count["value"] = count["value"]  + 1	


def savePreMove(direction, preMove):
	if direction == East or direction == West:
		preMove["x"] = direction
	if direction == North or direction == South:
		preMove["y"] = direction

def moveDrone(direction, preMove):
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
		savePreMove(direction, preMove)
		move(direction)
		return True

	# Пытаюсь спасти ситуацию
	if len(listMove) != 0:
		savePreMove(listMove[0], preMove)
		move(listMove[0])
	
	else:
		return False
			

# Позиция перемещения
def movePositionDinosaur(x,y,preMove):
	while True:
		xDrop = get_pos_x()
		yDrop = get_pos_y()

		if x > xDrop:
			if(moveDrone(East,preMove) == False):
				return False
			continue

		if x < xDrop:
			if(moveDrone(West,preMove) == False):
				return False
			continue

		if y > yDrop:
			if(moveDrone(North,preMove) == False):
				return False
			continue

		if y < yDrop:
			if(moveDrone(South,preMove) == False):
				return False
			continue

		if y == yDrop and x == xDrop:
			return True