def run(size = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)):
	print(str(North))
	listDirection = [North,East,South,West]
	listDirectionPath = [South,West,North,East]
	path = []
	list = {}
	while(True):
		# я в лабиринте
		if get_entity_type() == Entities.Hedge:
			x = get_pos_x()
			y = get_pos_y()
			# Создание клетки и определения путей
			if str(x) + str(y) not in list:
				list[str(x) + str(y)] = { }
				for itemDirection in listDirection:
					if(can_move(itemDirection)):
						list[str(x) + str(y)][str(itemDirection)] = True   
					else: 
						list[str(x) + str(y)][str(itemDirection)] = False 
			# Движения
			#x, y = measure()
			index = -1
			checkMove = False
			for itemDirection in listDirection:
				index = index + 1
				# Путь есть и если дрон пришел не оттуда
				if list[str(x) + str(y)][str(itemDirection)] and listDirectionPath[index] != itemDirection:
					list[str(x) + str(y)][str(itemDirection)] = False
					path.append(listDirectionPath[index])
					move(itemDirection)
					checkMove = True
					break

			if checkMove == False:
				move(path[len(path) - 1])
				path.pop()
				# Надо возвращаться назад нужно продолжать двигаться пока не путей по path
				continue
				 
						
		# Это сокровище
		if get_entity_type() == Entities.Treasure:
			harvest()
			   
		# не лабиринт
		if get_entity_type() != Entities.Hedge:
			# не трава
			if get_entity_type() != Entities.Bush:
				plant(Entities.Bush)

			# лабиринт готов к созданию
			if can_harvest() and get_entity_type() == Entities.Bush:
				use_item(Items.Weird_Substance, size)
		