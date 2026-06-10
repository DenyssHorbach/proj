from classes.VehicleLinkedList import VehicleLinkedList
from classes.Vehicle import Vehicle
from classes.VehicleType import VehicleType

test = Vehicle(VehicleType.HATCHBACK, 2.28, is_electric=True)

print(test)

test2 = VehicleLinkedList()
test2.insert_at(0, test)
print(test2)
test2.display_table()