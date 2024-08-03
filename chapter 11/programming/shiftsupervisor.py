
from Workers import ShiftSupervisor
def main():
    print("Enter Shift supervisor info")
    shiftsup = ShiftSupervisor(
        employee_name=input("Enter employee name: "),
        employee_number=input("Enter employee number: "),
        annual_production=int(input("Enter annual production: ")),
        annual_salary=float(input("Enter annual salary: "))
    )

    print("___________ INFO ______________")
    print("Name: ",shiftsup.get_employee_name())
    print("Number: ",shiftsup.get_employee_number())
    print("Annual prod: ",shiftsup.get_annual_production())
    print("Annual Salary: ",shiftsup.get_annuel_salary())


main()