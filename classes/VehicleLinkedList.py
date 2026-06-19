#!!!в ноль списано, потім розберусь!!!

from classes.Node import Node
import json
from classes.Vehicle import Vehicle
from classes.VehicleType import VehicleType


class VehicleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
        self._current_iterator_node = None  # Для методів ітерації (e)

    @property
    def length(self) -> int:
        return self._length

    def insert_at(self, index: int, vehicle: Vehicle):
        if index < 0 or index > self._length:
            raise IndexError("Index out of range")

        new_node = Node(vehicle)

        if self._length == 0:
            self._head = new_node
            self._tail = new_node
        elif index == 0:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        elif index == self._length:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        else:
            current = self._get_node_at(index)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

        self._length += 1

    # b) Метод видалення елемента з початку списку
    def remove_from_start(self) -> Vehicle:
        if self._head is None:
            raise IndexError("Impossible to remove from empty list")

        removed_data = self._head.data
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None

        self._length -= 1
        return removed_data

    # c) Читання індексатора та зміна значення
    def __getitem__(self, index: int) -> Vehicle:
        return self._get_node_at(index).data

    def __setitem__(self, index: int, vehicle: Vehicle):
        node = self._get_node_at(index)
        node.data = vehicle

    # Допоміжний метод для пошуку вузла за індексом з обробкою винятків
    def _get_node_at(self, index: int) -> Node:
        if index < 0 or index >= self._length:
            raise IndexError("Index put of range")

        # Оптимізація пошуку: з початку чи з кінця
        if index < self._length // 2:
            current = self._head
            for _ in range(index):
                current = current.next
        else:
            current = self._tail
            for _ in range(self._length - 1, index, -1):
                current = current.prev
        return current

    # e) Методи ітерації списку
    def start_iteration(self):
        """Метод отримання початкового значення ініціалізує ітератор"""
        self._current_iterator_node = self._head
        if self._current_iterator_node:
            return self._current_iterator_node.data
        return None

    def get_next_iteration(self):
        """Метод отримання наступного значення"""
        if self._current_iterator_node and self._current_iterator_node.next:
            self._current_iterator_node = self._current_iterator_node.next
            return self._current_iterator_node.data
        return None

    # f) Метод зворотного порядку елементів у списку (Реверс)
    def reverse(self):
        if self._length <= 1:
            return

        current = self._head
        self._tail = current  # Старий head стане новим tail

        prev_node = None
        while current is not None:
            # Міняємо місцями next та prev для кожного вузла
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node

            # Переходимо до наступного вузла (який тепер у current.prev)
            current = current.prev

        if prev_node is not None:
            self._head = prev_node.prev

    # g) Пошук елементів списку відповідно до завдання
    # Критерій: Електричні (гібридні) з об'ємом двигуна менше 2.0 л
    def search_special_vehicles(self) -> list:
        results = []
        current = self._head
        while current:
            if current.data.is_electric and current.data.engine_capacity < 2.0:
                results.append(current.data)
            current = current.next
        return results

    # Виведення у вигляді таблиці
    def display_table(self):
        if self._length == 0:
            print("[list is empty]")
            return
        print("-" * 50)
        print(f"{'№':<3} | {'Type':<15} | {'Engine capacity':<14} | {'Is electric':<10}")
        print("-" * 50)
        current = self._head
        idx = 0
        while current:
            print(f"{idx:<3} | {current.data}")
            current = current.next
        print("-" * 50)

    # Реалізація серіалізації в JSON
    def serialize_to_json(self, filename: str):
        data_list = []
        current = self._head
        while current:
            data_list.append({
                "type": current.data.vehicle_type.name,
                "capacity": current.data.engine_capacity,
                "is_electric": current.data.is_electric
            })
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

    # Реалізація десеріалізації з JSON
    def deserialize_from_json(self, filename: str):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data_list = json.load(f)

            # Очищуємо поточний список
            self._head = None
            self._tail = None
            self._length = 0

            for item in data_list:
                v_type = VehicleType[item["type"]]
                vehicle = Vehicle(v_type, item["capacity"], item["is_electric"])
                self.insert_at(self._length, vehicle)
        except FileNotFoundError:
            raise FileNotFoundError("File are not detected")