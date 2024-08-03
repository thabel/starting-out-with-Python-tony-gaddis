class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        Employee.__init__(self, employee_name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


class ShiftSupervisor(Employee):
    def __init__(
        self, employee_name, employee_number, annual_salary, annual_production
    ):
        Employee.__init__(self, employee_name, employee_number)
        self.__annual_salary = annual_salary
        self.__annual_production = annual_production

    def get_annuel_salary(self):
        return self.__annual_salary

    def get_annual_production(self):
        return self.__annual_production


def main():
    prodwork = ProductionWorker(
        employee_name=input("Enter employee name: "),
        employee_number=input("Enter employee number: "),
        shift_number=int(input("Enter shift number: ")),
        hourly_pay_rate=float(input("Enter hourly pay rate: ")),
    )

    print("___________ INFO ______________")
    print("Name: ", prodwork.get_employee_name())
    print("Number: ", prodwork.get_employee_number())
    print("Shitf: ", prodwork.get_shift_number())
    print("Pay rate: ", prodwork.get_hourly_pay_rate())

    print("Enter Shift supervisor info")


if __name__ == "__main__":
    main()
