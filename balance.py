import utils
import moveDrop

dronCactusX = 0
dronCactusY = 5

# Дрон для кактуса
def carrotDron(cactusPosX, cactusPosY, dronCactusMove):
	moveDrop.movePosition(cactusPosX, cactusPosY)
	list = {}
	while(True):
		# Узнать размеры
		moveDrop.movePosition(dronCactusX, dronCactusY)
		for index in range(get_world_size()):
			utils.updateGrounds()
			plant(Entities.Cactus)
			list[index] = measure()
			move(dronCactusMove)

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
				moveDrop.movePosition(minValueIndex, dronCactusY)
				while(True):
					x =  get_pos_x()
					if x != item:
						val = list[x]
						list[x] = list[x - 1]
						list[x - 1] = val
						swap(utils.listDirectionReverseObject[dronCactusMove])
						move((utils.listDirectionReverseObject[dronCactusMove]))
					if x == item:
						break
		moveDrop.movePosition(get_world_size() / 2, dronCactusY)				
		harvest()