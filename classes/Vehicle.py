from classes.VehicleType import VehicleType

class Vehicle:
    def __init__(self, vehicle_type: VehicleType, engine_capacity: float, is_electric: bool):
        self.vehicle_type = vehicle_type
        self.engine_capacity = engine_capacity
        self.is_electric = is_electric

    @property
    def vehicle_type(self) -> VehicleType:
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        # Перевіряємо, чи збігається ім'я класу або його базового класу з 'VehicleType'
        if type(value).__name__ != 'VehicleType' and not any(
                b.__name__ == 'VehicleType' for b in type(value).__bases__):
            raise TypeError("Incorrect type")
        self._vehicle_type = value

    @property
    def engine_capacity(self) -> float:
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, value: float):
        if value < 0:
            raise ValueError("Engine capacity can not be negative")
        self._engine_capacity = float(value)

    @property
    def is_electric(self) -> bool:
        return self._is_electric

    @is_electric.setter
    def is_electric(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("is_electric must be a boolean")
        self._is_electric = value

    def __str__(self):
        electric_str = "Yes" if self.is_electric else "No"
        return f"{self._vehicle_type.value:<15} | {self._engine_capacity:<14.1f} | {electric_str:<10}"