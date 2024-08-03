class Personal:
    def __init__(self, name:str, address:str, age:int, phone_number:str) -> None:
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def __str__(self) -> str:
        return f"Name:{self.__name},Address:{self.__address},Age:{self.__age},PhoneNumber:{self.__phone_number}"

def main():
    persons = {
        "me":Personal("Thabel","Casablanca , Firdaous",22,"+212643683602"),
        "Omar":Personal("Omar","Rabat , Maroc",43,"+212643683604"),
        "Oméga":Personal("Omega","Layoune ",19,"+212653683602"),
    }
    for data in persons.values():
        print(data)


main()