import utils

def generatorKeysList(x,y):
	return "x" + str(x) + "y" + str(y)

def run(size = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1), countMax = 5):
	path = []
	list = {}
	countCur = 0
	while(True):
		# я в лабиринте
		if get_entity_type() == Entities.Hedge:
			x = get_pos_x()
			y = get_pos_y()
			# Создание клетки и определения путей
			if generatorKeysList(x,y) not in list:
				list[generatorKeysList(x,y)] = { }
				for itemDirection in utils.listDirection:
					if(can_move(itemDirection)):
						list[generatorKeysList(x,y)][str(itemDirection)] = True   
					else: 
						list[generatorKeysList(x,y)][str(itemDirection)] = False 
			# Движения
			#x, y = measure()
			index = -1
			checkMove = False
			for itemDirection in utils.listDirection:
				index = index + 1
				# Путь есть и если дрон пришел не оттуда
				if list[generatorKeysList(x,y)][str(itemDirection)] and utils.listDirectionReverse[index] != itemDirection:
					list[generatorKeysList(x,y)][str(itemDirection)] = False
					path.append(utils.listDirectionReverse[index])
					move(itemDirection)
					checkMove = True
					break

			# Возвращаемся назад
			if checkMove == False:
				while(True):
					move(path[len(path) - 1])
					path.pop()
					xPath = get_pos_x()
					yPath = get_pos_y()

					checkMovePath = False

					for itemDirection in utils.listDirection:
						if list[generatorKeysList(xPath, yPath)][str(itemDirection)]:
							checkMovePath = True
					if checkMovePath:
						break
				continue
						
		# Это сокровище
		if get_entity_type() == Entities.Treasure:
			list = {}
			path = []
			countCur = countCur + 1
			if countCur == countMax:
				countCur = 0
				harvest()
			else:
				use_item(Items.Weird_Substance, size)

		# не лабиринт
		if get_entity_type() != Entities.Hedge:
			# не трава
			if get_entity_type() != Entities.Bush:
				harvest()
				plant(Entities.Bush)

			# лабиринт готов к созданию
			if can_harvest() and get_entity_type() == Entities.Bush:
				use_item(Items.Weird_Substance, size)
		