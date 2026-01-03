import moveDrop
import utils

# нужно переделать 1 дрон изучает лево право


# Общая логика проверки линии
def droneCheckLinia(multiplicity, checkType):
	pos = multiplicity
	list = {}
	moveType = None
	while True:	
		if pos > get_world_size() - 1:
			return True
		
		#  Определить место перемещения
		if checkType == "x":
			moveDrop.movePosition(0, pos)
			moveType = East
		else: 
			moveDrop.movePosition(pos, 0)
			moveType = North

		# создание кактусов
		for index in range(get_world_size()):
			if get_entity_type() != Entities.Cactus:
				harvest()
			utils.updateGrounds()
			plant(Entities.Cactus)
			list[index] = measure()
			move(moveType)

		# Попытки сортировать
		for item in range(get_world_size()):
			minValueIndex = None
			# Поиск минимального числа
			for findItem in range(get_world_size()):
				if findItem < item:
					continue

				if minValueIndex == None or list[minValueIndex] > list[findItem]:
					minValueIndex = findItem

			# Проверка что он есть
			if minValueIndex != None:
				if checkType == "x":
					moveDrop.movePosition(minValueIndex, pos)
				else:
					moveDrop.movePosition(pos, minValueIndex)

				while(True):
					posDrone = None
					if checkType == "x":
						posDrone = get_pos_x()
					else:
						posDrone = get_pos_y()
					if posDrone != item:
						val = list[posDrone]
						list[posDrone] = list[posDrone - 1]
						list[posDrone - 1] = val
						swap(utils.listDirectionReverseObject[moveType])
						move((utils.listDirectionReverseObject[moveType]))
					if posDrone == item:
						break

		pos = pos + max_drones()
		list = {}


# Движение дронов
def moveCactus(multiplicity):
	droneCheckLinia(multiplicity, "x")
	droneCheckLinia(multiplicity, "y")
	return True


def generatorDrone(listDrone):
	while(num_drones() < max_drones()):
		def funDrone():
			return moveCactus(num_drones() - 1)
		listDrone.append(spawn_drone(funDrone))

# старт функции
def run():
	# Бесконечно создавать дронов
	while(True):
		listDrone = []	
		generatorDrone(listDrone)
		moveCactus(0)
		
		# Бесконечно ждать когда все дроны выполнят свои задачи
		while(True):
			countTrue = 0
			for itemDrone in listDrone:
				check = has_finished(itemDrone)
				if check == False:
					break
				countTrue = countTrue + 1
			if countTrue == max_drones() - 1:
				break
		harvest()