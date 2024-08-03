"""
this program will be design as these
We will consider a set of predefined 
items to show to the user

And the user need just to buy 
different items 

when finished we will show him
the total price.

we will subtotal for each item
mutiplying by units in memory
"""

import RetailItem


class CashRegister:
    def __init__(self) -> None:
        self.__list_of_items: list[RetailItem.RetailItem] = []

    def purchase_item(self, item: RetailItem.RetailItem):
        self.__list_of_items.append(item)
        print("item purshased successfully")

    def get_total(self):
        tot = 0
        for item in self.__list_of_items:
            tot += item.get_sub_price()

        return tot

    def show_items(self):
        print(
            "{:<15} {:<10} {:<10} {:<10}".format(
                "description", "units", "price", "sub price"
            )
        )
        for item in self.__list_of_items:
            print(
                "{:<15} {:<10} {:<10} {:<10}".format(
                    item.get_item_description(),
                    item.get_units_in_inventory(),
                    item.get_price(),
                    item.get_sub_price(),
                )
            )

    def clear(self):
        self.__list_of_items = []
