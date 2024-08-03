class Pet:
    def __init__(self, name: str, animal_type: str, age: int) -> None:
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_animal_type(self):
        return self.__animal_type


def main():
    name, animal_type, age = (
        input("enter name: "),
        input("enter the animal type: "),
        int(input("Enter the age: ")),
    )
    pet = Pet(name, animal_type, age)
    print(
        f"INFO: pet name {pet.get_name()} , pet type {pet.get_animal_type()} , pet age {pet.get_age()}"
    )

main()