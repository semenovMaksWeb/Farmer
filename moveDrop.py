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