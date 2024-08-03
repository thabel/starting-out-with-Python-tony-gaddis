class Employee:
    def __init__(self, name, id_number, department, job_title) -> None:
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_id_number(self):
        return self.__id_number

    def get_job_title(self):
        return self.__job_title

    def __str__(self) -> str:
        return str(vars(self))


def main():
    employees = {
        "emp1": Employee("Susan Meyers", 47899, "Accounting", "Vice President"),
        "emp2": Employee("Mark Jones", 39119, "IT", "Programmer"),
        "emp3": Employee("Joy Rogers", 81774, "Manufacturing", "Engineer"),
    }
    for data in employees.values():
        print(data)


if __name__ == "__main__":
    main()
