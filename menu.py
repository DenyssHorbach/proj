from classes.Vehicle import Vehicle
from classes.VehicleType import VehicleType
from classes.VehicleLinkedList import VehicleLinkedList


def get_float_input(prompt: str):
    while True:
        try:
            val = float(input(prompt))
            if val < 0:
                print("Число не може бути від'ємним!")
                continue
            return val
        except ValueError:
            print("Помилка! Введіть дійсне число (наприклад, 1.6).")


def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Помилка! Введіть ціле число.")


def get_bool_input(prompt: str) -> bool:
    while True:
        val = input(prompt).strip().lower()
        if val in ['так', 'y', 'yes', '1']:
            return True
        if val in ['ні', 'n', 'no', '0']:
            return False
        print("Будь ласка, введіть 'так' або 'ні'.")


def input_vehicle() -> Vehicle:
    print("\nОберіть тип транспортного засобу:")
    types = list(VehicleType)
    for i, t in enumerate(types):
        print(f"{i} - {t.value}")

    while True:
        choice = get_int_input("Ваш вибір: ")
        if 0 <= choice < len(types):
            selected_type = types[choice]
            break
        print("Некоректний вибір типу. Спробуйте ще раз.")

    capacity = get_float_input("Введіть об'єм двигуна (напр. 1.6): ")
    is_elec = get_bool_input("Транспорт електричний/гібридний? (так/ні): ")
    return Vehicle(selected_type, capacity, is_elec)


# ========================================================
# ГОЛОВНА ФУНКЦІЯ МЕНЮ
# ========================================================

def run_menu(v_list: VehicleLinkedList):
    filename = "vehicles.json"

    while True:
        print("\n=== MENU ===")
        print("1. output list")
        print("2. add element by index")
        print("3. delete element from start")
        print("4. indexator")
        print("5. read element by index")
        print("6. show list length")
        print("7. print elements by iterator")
        print("8. reverse")
        print("9. finder")
        print("10. save to file")
        print("11. load from file")
        print("0. exit")

        choice = input("\nchoose action ").strip()

        try:
            if choice == "1":
                print("\nПоточний стан списку:")
                v_list.display_table()

            elif choice == "2":
                idx = get_int_input(f"Введіть індекс для вставки (0-{v_list.length}): ")
                vehicle = input_vehicle()  # Викликаємо функцію введення ТЗ
                v_list.insert_at(idx, vehicle)
                print("Елемент успішно додано!")
                v_list.display_table()

            elif choice == "3":
                removed = v_list.remove_from_start()
                print(f"Видалено елемент з початку: {removed}")
                v_list.display_table()

            elif choice == "4":
                if v_list.length == 0:
                    print("Список порожній!")
                    continue
                idx = get_int_input(f"Введіть індекс для зміни (0-{v_list.length - 1}): ")
                print("Введіть нові дані:")
                vehicle = input_vehicle()
                v_list[idx] = vehicle
                print("Значення змінено!")
                v_list.display_table()

            elif choice == "5":
                if v_list.length == 0:
                    print("Список порожній!")
                    continue
                idx = get_int_input(f"Введіть індекс (0-{v_list.length - 1}): ")
                print(f"Знайдено транспортний засіб: {v_list[idx]}")

            elif choice == "6":
                print(f"Поточна кількість вузлів у списку: {v_list.length}")

            elif choice == "7":
                print("\nІтерація списку від початку:")
                current_item = v_list.start_iteration()
                if current_item is None:
                    print("Список порожній.")
                while current_item:
                    print(f"-> {current_item}")
                    current_item = v_list.get_next_iteration()

            elif choice == "8":
                v_list.reverse()
                print("Список успішно перевернуто!")
                v_list.display_table()

            elif choice == "9":
                print("\nРезультати пошуку (Електричні ТЗ з двигуном < 2.0л):")
                search_res = v_list.search_special_vehicles()
                if not search_res:
                    print("Нічого не знайдено.")
                for item in search_res:
                    print(item)

            elif choice == "10":
                v_list.serialize_to_json(filename)
                print(f"Дані успішно збережено у файл '{filename}'")

            elif choice == "11":
                v_list.deserialize_from_json(filename)
                print(f"Дані успішно завантажено з файлу '{filename}'")
                v_list.display_table()

            elif choice == "0":
                print("Вихід з програми. Гарного дня!")
                break
            else:
                print("Некоректний вибір! Спробуйте ще раз.")

        except (IndexError, ValueError, FileNotFoundError) as ex:
            print(f"\n⚠️ [ОБРОБКА ВИКЛЮЧЕННЯ]: {ex}")
        except Exception as e:
            print(f"\n⚠️ Непередбачена помилка: {e}")