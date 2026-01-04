import utils

def generatorKeys(x,y):
	return "x" + str(x) + "y" + str(y)


def run():
	list = {}
	set_world_size(3)
	while True:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				utils.movePosition(x, y)
				plant_type, (x, y) = get_companion()
				list[generatorKeys(x,y)] = {"type": plant_type}
		print(list)
		
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if generatorKeys(x,y) in list:
					utils.movePosition(x, y)
					utils.updateGrounds()
					utils.water(0.8)
					plant(list[generatorKeys(x,y)]["type"])
		
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				utils.movePosition(x, y)
				utils.waitHarvest()
				plant(Entities.Grass)