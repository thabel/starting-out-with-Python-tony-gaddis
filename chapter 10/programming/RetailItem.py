class RetailItem:
    def __init__(self, item_description:str, units_in_inventory:int, price:float) -> None:
        self.__item_description = item_description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    def get_item_description(self):
        return self.__item_description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price

    def get_sub_price(self):
        return self.__price*self.__units_in_inventory
    
    def __str__(self) -> str:
        return str(vars(self))


def main():
    employees = {
        "item1": RetailItem("Jacket", 12, 59.95),
        "item2": RetailItem("Designer Jeans", 40, 34.95),
        "item3": RetailItem("Shirt" ,20, 24.95),
    }
    for data in employees.values():
        print(data)

if __name__ == "__main__":
    main()
