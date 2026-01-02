listDirection = [North,East,South,West]
listDirectionReverse = [South,West,North,East]

listDirectionReverseObject = {North:South, East:West, South:North, West:East }

def updateGrounds():
	if get_ground_type() != Grounds.Soil:
		till()

def water(value = 0.5):
	
	if get_water() >= value:
		return
	
	if num_items(Items.Water) == 0:
		return
	
	use_item(Items.Water)
 
def waitHarvest():
	while True:
		if can_harvest():
			harvest()
			break

def fertilizer():
	if num_items(Items.Fertilizer) > 10:
		use_item(Items.Fertilizer)

def checkHarvest():
	if can_harvest():
		harvest()