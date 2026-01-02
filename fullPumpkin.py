import utils
import moveDrop

def run():
	while True:
		moveDrop.movePosition(0,0)
		for row in range(get_world_size()):
			for col in range(get_world_size()):
				checkPumpkin()
				move(North)
			move(East)
		if get_entity_type() == Entities.Pumpkin:
			utils.waitHarvest()
		else:
			harvest()

def checkPumpkin():
	while True:			
		if get_entity_type() != Entities.Pumpkin:
			harvest()
			utils.updateGrounds()
			plant(Entities.Pumpkin)
		elif get_entity_type() == Entities.Pumpkin:
			break