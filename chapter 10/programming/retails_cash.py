import CashRegister
import RetailItem


LIST_OF_ITEMS = {
    "Jacket": RetailItem.RetailItem("Jacket", 12, 59.95),
    "Jeans": RetailItem.RetailItem("Designer Jeans", 40, 34.95),
    "Shirt": RetailItem.RetailItem("Shirt", 20, 24.95),
}
QUIT = "q"
number_retail = {}


def show_items_to_user():
    print()
    print(
        "   {:<5} {:<15} {:<15} {:<15}".format(
            "N°",
            "Description",
            "Units",
            "price",
        )
    )
    print()
    for i, item_name in enumerate(LIST_OF_ITEMS.keys()):
        number_retail[i + 1] = LIST_OF_ITEMS[item_name]
        print(
            "   {:<5} {:<15} {:<15} {:<15}".format(
                "#" + str(i + 1) + ".",
                item_name,
                LIST_OF_ITEMS[item_name].get_units_in_inventory(),
                LIST_OF_ITEMS[item_name].get_price(),
            )
        )
    print()


def get_user_choice():
    while True:
        try:
            string = input("Choose item number or q to quit: ")
            u_choice = int(string)
        except ValueError:
            if string == QUIT:
                return string
            continue
        if u_choice <= len(LIST_OF_ITEMS) or u_choice >= 1:
            break
        print("Bad input , Try again.")
    return u_choice


def main():
    cash_register = CashRegister.CashRegister()
    show_items_to_user()
    choice = get_user_choice()
    while choice != QUIT:
        cash_register.purchase_item(number_retail[choice])
        show_items_to_user()
        choice = get_user_choice()
    print("________________ BILL ____________________")
    cash_register.show_items()
    print("Final Total ....", cash_register.get_total())


if __name__ == "__main__":
    main()
