import moveDrop
import utils

# нужно переделать 1 дрон изучает лево право

# Движение дронов
def movePumpkin(multiplicity):
	posY = multiplicity
	list = {}
	count = 0
	while True:	
		if posY > get_world_size() - 1:
			print(count)
			return True
		moveDrop.movePosition(posY, 0)
		# создание кактусов
		for index in range(get_world_size()):
			if get_entity_type() != Entities.Cactus:
				harvest()
			utils.updateGrounds()
			plant(Entities.Cactus)
			if measure() == 0:
				count = count + 1
			list[index] = measure()
			move(North)
	
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
				moveDrop.movePosition(posY, minValueIndex)
				while(True):
					y =  get_pos_y()
					if y != item:
						val = list[y]
						list[y] = list[y - 1]
						list[y - 1] = val
						swap(utils.listDirectionReverseObject[North])
						move((utils.listDirectionReverseObject[North]))
					if y == item:
						break

		posY = posY + max_drones()
		list = {}


def generatorDrone(listDrone):
	while(num_drones() < max_drones()):
		def funDrone():
			return movePumpkin(num_drones() - 1)
		listDrone.append(spawn_drone(funDrone))

# старт функции
def run():
	# Бесконечно создавать дронов
	while(True):
		listDrone = []	
		generatorDrone(listDrone)
		movePumpkin(0)
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