import utils

# Создать лабиринт
def createHedge(size):
	# не лабиринт
	if get_entity_type() != Entities.Hedge:
		# не трава
		if get_entity_type() != Entities.Bush:
			harvest()
			plant(Entities.Bush)
		# лабиринт готов к созданию
		if can_harvest() and get_entity_type() == Entities.Bush:
			use_item(Items.Weird_Substance, size)

# забрать сокровища
def harvestTreasure(size):
	use_item(Items.Weird_Substance, size)

def run(size = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)):
	preMove = None
	while True:
		createHedge(size)
		harvestTreasure(size)
		listMove = []
		for itemDirection in utils.listDirection:
			if can_move(itemDirection) and preMove != utils.listDirectionReverseObject[itemDirection]:
				listMove.append(itemDirection)
		if len(listMove) == 1:
			preMove = listMove[0]
			move(listMove[0])
		else:
			index = -1
			for moveItem in listMove:
				index = index + 1
				if index == len(listMove) - 1:
					move(listMove[len(listMove) - 1])
				else:
					generatorDrone(moveItem)

# Создание дронов в лабиринте
def generatorDrone(itemDirection):
	def droneFun():
		moveDroneCheck(itemDirection)
	if max_drones() != num_drones():
		spawn_drone(droneFun)
	else:
		while True:
			if max_drones() != num_drones():
				spawn_drone(droneFun)
				break

def moveDroneCheck(moveDrone):
	move(moveDrone)
	for itemDirection in utils.listDirection:
			if(can_move(itemDirection) and moveDrone != itemDirection):
				generatorDrone(itemDirection)
	return True