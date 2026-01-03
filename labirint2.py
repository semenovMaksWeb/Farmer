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
	preMove = { "value": None }
	while True:
		funDrone(size)

# Возвращает список куда можно переместить дрона
def getListPath():
	listMove = {}
	for itemDirection in utils.listDirection:
		if(can_move(itemDirection)):
			listMove[itemDirection] = True

# Определения движения дрона
def moveDrone(moveList, preValue):
	# if moveList[]
	return

# общая функция на дронов
def funDrone(size, preMove):
	createHedge(size) # Проверка и создание лабиринта
	harvestTreasure(size) # забрать сокровище
	moveList = getListPath() # Узнать путь куда можно двигаться
	
	# Путь 1 идем это тупик
	if len(moveList) == 1 and preMove["value"] != None:
		# Уничтожить дрона
		return
	
	# есть 1 путь
	if len(moveList) == 2 and preMove["value"] != None and preMove["value"] == utils.listDirectionReverseObject[preMove["value"]]:
		move()