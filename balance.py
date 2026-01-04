import utils

countGrass = 7 # Кол-во строк для фарма травы
countSunflower = 10 # Кол-во строк для фарма энергии
countTree = 5 # Кол-во строк для фарма дерева
countCarrot = 10 # Кол-во строк для фарма моркови

# Логика перемещения дрона
def moveDron(xStart, xEnd, yStart, yEnd):
	x = get_pos_x()
	y = get_pos_y()

	if x == xEnd and y == yEnd:
		x = xStart
		y = yStart
		utils.movePosition(x,y)
		return
	
	if x == xEnd:
		x = 0
		y = y + 1
		utils.movePosition(x,y)
		return

	x = x + 1
	utils.movePosition(x,y)

# Функция вызова дрона фарм энергии нужно переделать на поиск max
def droneTreeMany(XStart, XEnd, YStart, YEnd):
	def fun():
		utils.movePosition(XStart, YStart)
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
			moveDron(XStart, XEnd, YStart, YEnd)
	spawn_drone(fun)

# Функция вызова дрона фарм травы
def droneGrassMany(XStart, XEnd, YStart, YEnd):
	def fun():
		utils.movePosition(XStart, YStart)
		while True:
			utils.checkHarvest()
			plant(Entities.Grass)
			moveDron(XStart, XEnd, YStart, YEnd)
	spawn_drone(fun)


# Функция вызова дрона фарм энергии
def droneSunflowerMany(XStart, XEnd, YStart, YEnd):
	def fun():
		utils.movePosition(XStart, YStart)
		while True:
			utils.water()
			utils.checkHarvest()
			utils.updateGrounds()
			plant(Entities.Sunflower)
			moveDron(XStart, XEnd, YStart, YEnd)
	spawn_drone(fun)

def droneCarrotMany(XStart, XEnd, YStart, YEnd):
	def fun():
		utils.movePosition(XStart, YStart)
		while True:
			utils.water()
			utils.checkHarvest()
			utils.updateGrounds()
			plant(Entities.Carrot)
			moveDron(XStart, XEnd, YStart, YEnd)
	spawn_drone(fun)

# Общая функция старта
def run():
	# Энергия
	start = 0
	for i in range(countSunflower):
		droneSunflowerMany(0, get_world_size() - 1, start + i, start + i)

	# Трава
	start = start + countSunflower
	for i in range(countGrass):
		droneGrassMany(0, get_world_size() - 1, start + i, start + i)
	
	# Дерево
	start = start + countGrass
	for i in range(countTree):
		droneTreeMany(0, get_world_size() - 1, start + i, start + i)

	# Мокровь
	start = start + countTree
	for i in range(countCarrot):
		droneCarrotMany(0, get_world_size() - 1, start + i, start + i)