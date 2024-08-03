class Person:
    def __init__(self, name, address, tel_phone):
        self.__name = name
        self.__address = address
        self.__tel_phone = tel_phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_tel_phone(self):
        return self.__tel_phone


class Custumer(Person):
    def __init__(self, name, address, tel_phone, customer_member, be_on_mailing_list):
        Person.__init__(self, name, address, tel_phone)
        self.__customer_member = customer_member
        self.__be_on_mailing_list = be_on_mailing_list

    def get_customer_member(self):
        return self.__customer_member

    def get_be_on_mailing_list(self):
        return self.__be_on_mailing_list


def get_bool_data():
    data = input("Be on mailing? y or n: ")
    while data not in "ny":
        data = input("Be on mailing? y or n: ")
    if data == "y":
        return True
    else:
        return False


def main():
    customer = Custumer(
        name=input("Enter customer name: "),
        address=input("Enter customer address: "),
        tel_phone=input("Enter customer tel phone: "),
        customer_member=input("Enter customer member: "),
        be_on_mailing_list=get_bool_data(),
    )
    print("___________ INFO ______________")
    print("Name: ", customer.get_name())
    print("Address: ", customer.get_address())
    print("Telphone: ", customer.get_tel_phone())
    print("Customer member: ", customer.get_customer_member())
    print("Be on mailing list? ", customer.get_be_on_mailing_list())

main()