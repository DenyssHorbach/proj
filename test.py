from classes.Vehicle import Vehicle
from classes.VehicleType import VehicleType
from classes.VehicleLinkedList import VehicleLinkedList


test_car = Vehicle(VehicleType.TRUCK, 1.0, is_electric=True)
test_car2 = Vehicle(VehicleType.HATCHBACK, 1.6, is_electric=False)
test_car3 = Vehicle(VehicleType.SEDAN, 1.2, is_electric=True)
test_car4 = Vehicle(VehicleType.TRUCK, 1.0, is_electric=False)

test2 = VehicleLinkedList()
test2.insert_at(0, test_car)
test2.insert_at(1, test_car2)
test2.insert_at(2, test_car3)
test2.insert_at(3, test_car4)