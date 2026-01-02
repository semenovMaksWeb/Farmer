import utils
import moveDrop

# Деление участка на секции для получения всех ресурсов

# Конфиг травы
grassPosY = [1, 3,6,9, 11]
grassPosX = True

# Конфиг кусты и деревья
treePosY = [2, 5,7]
treePosX = True

# Конфиг морковь
carrotPosY = [4,8]
carrotPosX = True

# Конфиг энергии
sunflowerPosY = [0,10]
sunflowerPosX = True

# проверка конфига что сажать
def checkConfig(type):
	if type == "grass":
		return checkVal(grassPosX, grassPosY)
	if type == "tree":
		return checkVal(treePosX, treePosY)
	if type == "carrot":
		return checkVal(carrotPosX, carrotPosY)
	if type == "sunflower":
		return checkVal(sunflowerPosX, sunflowerPosY)

	return checkVal(grassPosX, grassPosY)

# Вспомогательная функция проверяющая конфиг массива что нужно сажать
def checkArray(arr, type):
	pos = None
	result = False
	if type == "x":
		pos = get_pos_x()
	if type == "y":
		pos = get_pos_y()
	
	for item in arr:
		if item == pos:
			result = True
			break
	return result

# Вспомогательная функция определяющая конфиг условия
def checkVal(arrX, arrY):
	resultCheckX = False
	resultCheckY = False
	if arrX == True:
		resultCheckX = True
	
	if arrY == True:
		resultCheckY = True   
	
	if arrX != True:
		resultCheckX = checkArray(arrX, "x")

	if arrY != True:
		resultCheckY =  checkArray(arrY, "y")

	return resultCheckY and resultCheckX

def run():
	while True:
		if can_harvest():
			harvest()
		yDrop = get_pos_y()
		xDrop = get_pos_x()

		if checkConfig("sunflower"):
			plant(Entities.Sunflower)	
  
		if checkConfig("grass"):
			plant(Entities.Grass)

		#  Растет кусты и деревья
		if checkConfig("tree"):
			if xDrop % 2 == 0:
				plant(Entities.Tree)
				utils.water()
			else:
				plant(Entities.Bush)
				utils.fertilizer()	
		# Растет морковь
		if checkConfig("carrot"):
			utils.updateGrounds()
			plant(Entities.Carrot)
			utils.water()

		yDrop = yDrop + 1 
		if yDrop > get_world_size() - 1:
			yDrop = 0
			xDrop = xDrop + 1
	
		if xDrop > get_world_size() - 1:
			xDrop = 0
			yDrop = 0
	
		moveDrop.movePosition(xDrop, yDrop)