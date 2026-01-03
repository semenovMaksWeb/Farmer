import utils

def harvestDinosaur(count):
	change_hat(Hats.Cactus_Hat)
	count["value"] =  0
	change_hat(Hats.Dinosaur_Hat)

def run():
	clear()
	harvest()
	count = {"value": 0}
	change_hat(Hats.Dinosaur_Hat)
	while True:
		next_x, next_y = measure()
		if movePositionDinosaur(next_x, next_y, count) == False:
			harvestDinosaur(count)
			continue
		movePositionDinosaur(next_x, next_y, count)
		count["value"] = count["value"]  + 1
		if count["value"] >= get_world_size() * 2:
			harvestDinosaur(count)

def moveDrone(direction, count):
	if move(direction) == False:
		checkAll = False
		for itemDirection in utils.listDirection:
			if move(itemDirection):
				checkAll = True
				break
		if checkAll == False:
			return False
			

# Позиция перемещения
def movePositionDinosaur(x,y,count):
	while True:
		xDrop = get_pos_x()
		yDrop = get_pos_y()

		if x > xDrop:
			if(moveDrone(East,count) == False):
				return False
			continue

		if x < xDrop:
			if(moveDrone(West,count) == False):
				return False
			continue

		if y > yDrop:
			if(moveDrone(North,count) == False):
				return False
			continue

		if y < yDrop:
			if(moveDrone(South,count) == False):
				return False
			continue

		if y == yDrop and x == xDrop:
			return True