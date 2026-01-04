listDirection = [North,East,South,West]
listDirectionReverse = [South,West,North,East]

listDirectionReverseObject = {North:South, East:West, South:North, West:East }

# Генерация ключа
def generatorKeys(x,y):
	return "x" + str(x) + "y" + str(y)

# Сменить грунт
def updateGrounds():
	if get_ground_type() != Grounds.Soil:
		till()

# Использовать воду
def water(value = 0.5):
	
	if get_water() >= value:
		return
	
	if num_items(Items.Water) == 0:
		return
	
	use_item(Items.Water)

# Ожидать пока появится потом забрать
def waitHarvest():
	while True:
		if can_harvest():
			harvest()
			break

# Использовать удобрения
def fertilizer():
	if num_items(Items.Fertilizer) > 10:
		use_item(Items.Fertilizer)

# Проверка что есть лут и забрать
def checkHarvest():
	if can_harvest():
		harvest()

# Позиция перемещения
def movePosition(x,y):
	while True:
		xDrop = get_pos_x()
		yDrop = get_pos_y()
  
		if x > xDrop:
			move(East)
			continue

		if x < xDrop:
			move(West)
			continue

		if y > yDrop:
			move(North)
			continue

		if y < yDrop:
			move(South)
			continue

		if y == yDrop and x == xDrop:
			break