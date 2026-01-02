import moveDrop

while True:
	if can_harvest():
		harvest()

	yDrop = get_pos_y()
	xDrop = get_pos_x()

	#  Растет трава
	if yDrop == 0:
		plant(Entities.Grass)

	#  Растет кусты и деревья
	if (yDrop == 1 or yDrop == 3) and can_harvest() == False:
		if xDrop % 2 == 0:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
	
	# Растет морковь
	if yDrop == 2 and can_harvest() == False:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)

	yDrop = yDrop + 1
 
	if yDrop > get_world_size() - 1:
		yDrop = 0
		xDrop = xDrop + 1
 
	if xDrop > get_world_size() - 1:
		xDrop = 0
		yDrop = 0
  
	moveDrop.movePosition(xDrop, yDrop)
	# do_a_flip()
	# pet_the_piggy()


 