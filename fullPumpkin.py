import moveDrop
import utils


# Ожидание появление тыквы
def waitPumpkin():
	while(True):
		if (
			(can_harvest() and get_entity_type() != Entities.Pumpkin) 
			or get_entity_type() == None
			or get_entity_type() == Entities.Dead_Pumpkin
		):
			harvest()
			plant(Entities.Pumpkin)
		elif(can_harvest() and get_entity_type() == Entities.Pumpkin):
			break
		else:
			utils.water(0.8)

# Движение дронов
def movePumpkin(multiplicity):
	posY = multiplicity
	while True:	
		if posY > get_world_size() - 1:
			return True
		moveDrop.movePosition(0, posY)
		for row in range(get_world_size()):
			utils.updateGrounds()
			waitPumpkin()
			move(East)

		posY = posY + max_drones()	


def generatorDrone(listDrone):
	while(num_drones() < max_drones()):
		def funDrone():
			return movePumpkin(num_drones() - 1)
		listDrone.append(spawn_drone(funDrone))

# старт функции
def run():
	# Бесконечно создавать дронов
	while(True):
		listDrone = []	
		generatorDrone(listDrone)
		movePumpkin(0)
		# Бесконечно ждать когда все дроны выполнят свои задачи
		while(True):
			for itemDrone in listDrone:
				check = has_finished(itemDrone)
				if check == False:
					break
			break
		harvest()