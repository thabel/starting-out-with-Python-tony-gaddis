import pickle

from dayByDayCli.afficheHelper import take_good_input


def menu():
    print("1- see the list of all vegetables and their prices")
    print("2- add new vegetables")
    print("3- change the price of an existing vegetable")
    print("4- delete an existing vegetable and price")
    print("5- quit")


def vegetable_dict():
    try:
        with open("vegetables.dat", "rb") as f:
            veg_dict = pickle.load(f)
            return veg_dict
    except FileNotFoundError:
        with open("vegetables.dat", "wb"):
            return dict()


def save_in_file(veg_dict):
    with open("vegetables.dat", "wb") as f:
        pickle.dump(veg_dict, f)


def main():
    menu()
    try:
        user_choice = take_good_input('12345')
        veg_dict = vegetable_dict()
        while user_choice != '5':
            if user_choice == '1':
                if len(veg_dict) == 0:
                    print("Any vegetable added yet")
                else:
                    print(f"vegetables{'.' * 10}prices")
                    for k, v in veg_dict.items():
                        print(f"{k} {'.' * 10} {v}")
            elif user_choice == '2':
                veg_name = input("Enter vegetable name: ")
                veg_price = float(input("Enter vegetable price: "))
                if veg_name in veg_dict:
                    print(f'f{veg_name} already present want to modify price ?: ')
                    y_n_choice = take_good_input('yn')
                    if y_n_choice == 'y':
                        veg_dict[veg_name] = veg_price
                        print("Vegetables update successfully")
                else:
                    veg_dict[veg_name] = veg_price
                    print("Vegetables added successfully")
            elif user_choice == '3':
                veg_name = input("Enter vegetable name ")
                if veg_name in veg_dict:
                    veg_price = float(input("Enter vegetable new price: "))
                    veg_dict[veg_name] = veg_price
                    print("Price update succesffuly")
                else:
                    print(f"Vegetable of name {veg_name} is not found")

            else:
                veg_name = input("Enter vegetable name ")
                if veg_name in veg_dict:
                    veg_dict.pop(veg_name)
                    print("Vegetable deleted successfully")
                else:
                    print(f"Vegetable of name {veg_name} is not found")

            menu()
            user_choice = take_good_input('12345')
        save_in_file(veg_dict)
        print("Bye")
    except KeyboardInterrupt:
        save_in_file(veg_dict)


if __name__ == '__main__':
    main()
