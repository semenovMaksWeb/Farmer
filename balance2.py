import moveDrop
import utils

# Конфиг травы
grassYStart = 2
grassYEnd = 2
grassXStart = 0
grassXEnd = get_world_size() - 1


# Конфиг подсолнуха
sunflowerYStart = 0
sunflowerYEnd = 1
sunflowerXStart = 0
sunflowerXEnd = get_world_size() - 1

# Конфиг дерева
treeYStart = 3
treeYEnd = 4
treeXStart = 0
treeXEnd = get_world_size() - 1

# Конфиг морковки
carrotYStart = 5
carrotYEnd = 6
carrotXStart = 0
carrotXEnd = get_world_size() - 1


# Логика перемещения дрона
def moveDron(xStart, xEnd, yStart, yEnd):
	x = get_pos_x()
	y = get_pos_y()

	if x == xEnd and y == yEnd:
		x = xStart
		y = yStart
		moveDrop.movePosition(x,y)
		return
	
	if x == xEnd:
		x = 0
		y = y + 1
		moveDrop.movePosition(x,y)
		return

	x = x + 1
	moveDrop.movePosition(x,y)


# Функция вызова дрона фарм травы
def droneGrass():
	moveDrop.movePosition(grassXStart, grassYStart)
	while True:
		utils.checkHarvest()
		plant(Entities.Grass)
		moveDron(grassXStart, grassXEnd, grassYStart, grassYEnd)

# Функция вызова дрона фарм дерева
def droneTree():
	moveDrop.movePosition(treeXStart, treeYStart)
	while True:
		x = get_pos_x()
		y = get_pos_y()

		if (y % 2 == 0 and x %2 != 0) or (y % 2 != 0 and x %2 == 0):
			utils.checkHarvest()
			plant(Entities.Tree)
			utils.water()
		else:
			utils.checkHarvest()
			plant(Entities.Bush)
			utils.fertilizer()

		moveDron(treeXStart, treeXEnd, treeYStart, treeYEnd)

# Функция вызова дрона фарм энергии нужно переделать на поиск max
def droneSunflower():
		moveDrop.movePosition(sunflowerXStart, sunflowerYStart)
		while True:
			utils.water()
			utils.checkHarvest()
			utils.updateGrounds()
			plant(Entities.Sunflower)
			moveDron(sunflowerXStart, sunflowerXEnd, sunflowerYStart, sunflowerYEnd)


# Функция вызова дрона фарм энергии нужно переделать на поиск max
def droneCarrot():
	moveDrop.movePosition(carrotXStart, carrotYStart)
	while True:
		utils.checkHarvest()
		utils.updateGrounds()
		plant(Entities.Carrot)
		utils.water()
		moveDron(carrotXStart, carrotXEnd, carrotYStart, carrotYEnd)

# Общая функция старта
def run():
	spawn_drone(droneGrass)
	spawn_drone(droneTree)
	spawn_drone(droneCarrot)
	droneSunflower()