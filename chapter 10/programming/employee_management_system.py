import pickle
import Employee

FILE_NAME = "employees.dat"
QUIT = 6


def menu():
    print("Employee mananagement system")
    print("1. Look up an employee in the dictionary")
    print("2. Add a new employee to the dictionary")
    print("3. Change an existing employee’s name, department, and job title")
    print("4. Delete an employee from the dictionary")
    print("5. how many employees ?")
    print("6. Quit the program")

def how_many(employees_data:dict):
    print(f"there {len(employees_data)} employees")

def lookup(employees_data:dict):
    """lookup for employee using id"""
    emp_id = input("Enter employee id: ")
    print(employees_data.get(emp_id, f"{emp_id} not found"))


def delete_employee(employees_data:dict):
    emp_id = input("Enter employee id: ")
    if emp_id in employees_data:
        del employees_data[emp_id]
        print(f"employee with id {emp_id} deleteted")
    else:
        print(f"{emp_id} not found")


def change_employee(employees_data:dict):
    emp_id = input("Enter employee id: ")
    if emp_id in employees_data:
        name, department, job_title = (
            input("Enter employee Name: "),
            input("Enter employee department: "),
            input("Enter employee job title: "),
        )
        emp = Employee.Employee(
            name=name, id_number=emp_id, department=department, job_title=job_title
        )
        employees_data[emp_id] = emp
        print("Employee Changed")
    else:
        print(f"{emp_id} not found")


def add_new_employee(employees_data:dict):
    id_number, name, department, job_title = (
        input("Enter employee ID: "),
        input("Enter employee Name: "),
        input("Enter employee department: "),
        input("Enter employee job title: "),
    )
    emp = Employee.Employee(
        name=name, id_number=id_number, department=department, job_title=job_title
    )
    employees_data[id_number] = emp
    print("Employee saved")


def get_user_choice():
    while True:
        try:
            u_choice = int(input("Enter your choice: "))
        except ValueError:
            continue
        if u_choice <= QUIT or u_choice >= 1:
            break
        print("Bad input , Try again.")
    return u_choice


def load_employees_data():
    try:
        with open(FILE_NAME, "rb") as f:
            data = pickle.load(f)
    except IOError:
        data = {}
    return data


def save_data(employees_data):
    with open(FILE_NAME, "wb") as f:
        pickle.dump(employees_data, file=f)


MENU_CHOICES_FUNCTIONS = [lookup, add_new_employee, change_employee, delete_employee,how_many]


def main():
    # print the menu to the user
    empoyees_data = load_employees_data()
    menu()
    choice = get_user_choice()
    while choice != QUIT:
        MENU_CHOICES_FUNCTIONS[choice-1](empoyees_data)
        choice = get_user_choice()
    save_data(employees_data=empoyees_data)


if __name__ == "__main__":
    main()
