from classes.Vehicle import Vehicle
from classes.VehicleType import VehicleType
from classes.VehicleLinkedList import VehicleLinkedList


def get_float_input(prompt: str):
    while True:
        try:
            val = float(input(prompt))
            if val < 0:
                print("Num cannot be negative")
                continue
            return val
        except ValueError:
            print("Error, please enter a number")


def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a number")


def get_bool_input(prompt: str) -> bool:
    while True:
        val = input(prompt).strip().lower()
        if val in ['y', 'yes', '1']:
            return True
        if val in ['n', 'no', '0']:
            return False
        print("Enter yes or no.")


def input_vehicle() -> Vehicle:
    print("\nChoose type of vehicle.")
    types = list(VehicleType)
    for i, t in enumerate(types):
        print(f"{i} - {t.value}")

    while True:
        choice = get_int_input("your choice: ")
        if 0 <= choice < len(types):
            selected_type = types[choice]
            break
        print("incorrect type")

    capacity = get_float_input("enter egine capacity: ")
    is_elec = get_bool_input("electric / hybrid (yes or no): ")
    return Vehicle(selected_type, capacity, is_elec)


def main():
    v_list = VehicleLinkedList()
    filename = "vehicles.json"

    # Демонстраційне автозаповнення, щоб не клацати меню спочатку
    try:
        v_list.insert_at(0, Vehicle(VehicleType.SEDAN, 1.5, True))
        v_list.insert_at(1, Vehicle(VehicleType.SUV, 2.5, False))
        v_list.insert_at(2, Vehicle(VehicleType.HATCHBACK, 1.2, True))
        v_list.insert_at(3, Vehicle(VehicleType.TRUCK, 3.0, True))
    except Exception as e:
        print(f"init error: {e}")

    while True:
        print("\n=== ATD menu ===")
        print("1. output list")
        print("2. add element by index")
        print("3. delete element from start")
        print("4. correct element by index")
        print("5. read element by index")
        print("6. show list length")
        print("7. out element")
        print("8. reverse")
        print("9. search")
        print("10. save")
        print("11. download")
        print("0. exit")

        choice = input("\nchoose action: ").strip()

        try:
            if choice == "1":
                print("\nlist:")
                v_list.display_table()

            elif choice == "2":
                idx = get_int_input(f"enter index (0-{v_list.length}): ")
                vehicle = input_vehicle()
                v_list.insert_at(idx, vehicle)
                print("element added")
                v_list.display_table()

            elif choice == "3":
                removed = v_list.remove_from_start()
                print(f"element deleted from start: {removed}")
                v_list.display_table()

            elif choice == "4":
                if v_list.length == 0:
                    print("list is empty")
                    continue
                idx = get_int_input(f"enter index to correct (0-{v_list.length - 1}): ")
                print("new data:")
                vehicle = input_vehicle()
                v_list[idx] = vehicle
                print("corrected")
                v_list.display_table()

            elif choice == "5":
                if v_list.length == 0:
                    print("list is empty")
                    continue
                idx = get_int_input(f"enter index (0-{v_list.length - 1}): ")
                print(f"transport found: {v_list[idx]}")

            elif choice == "6":
                print(f"num of ...: {v_list.length}")

            elif choice == "7":
                print("\niteration from start:")
                current_item = v_list.start_iteration()
                if current_item is None:
                    print("list is empty")
                while current_item:
                    print(f"-> {current_item}")
                    current_item = v_list.get_next_iteration()

            elif choice == "8":
                v_list.reverse()
                print("list is reversed:")
                v_list.display_table()

            elif choice == "9":
                print("\nresult of finding:")
                search_res = v_list.search_special_vehicles()
                if not search_res:
                    print("nothing found.")
                for item in search_res:
                    print(item)

            elif choice == "10":
                v_list.serialize_to_json(filename)
                print(f"data was saved '{filename}'")

            elif choice == "11":
                v_list.deserialize_from_json(filename)
                print(f"data was downloaded from file'{filename}'")
                v_list.display_table()

            elif choice == "0":
                print("exit")
                break
            else:
                print("incorrect choice")

        except (IndexError, ValueError, FileNotFoundError) as ex:
            print(f"\nprocessing: {ex}")
        except Exception as e:
            print(f"\nunexpected error: {e}")


if __name__ == "__main__":
    main()