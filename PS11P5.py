employee_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]
employee_salaries = [50000, 60000, 55000, 58000, 62000, 47000, 75000, 52000, 49000, 68000]

def display_employees(names, salaries):
    print("\nEmployee Names and Salaries:")
    for i in range(len(names)):
        print(f"{names[i]} - ${salaries[i]:,.2f}")

def display_employees_reverse(names):
    print("\nEmployees in Reverse Order:")
    for name in reversed(names):
        print(name)

def find_highest_salary(names, salaries):
    highest_salary = max(salaries)
    index = salaries.index(highest_salary)
    print(f"\nHighest Salary: ${highest_salary:,.2f} by {names[index]}")

def sum_total_salary(salaries):
    total_salary = sum(salaries)
    print(f"\nTotal Salary Expense: ${total_salary:,.2f}")

def search_employee(names, salaries):
    while True:
        search_name = input("\nEnter an employee last name (or type 'exit' to quit): ").strip()
        if search_name.lower() == "exit":
            break
        if search_name in names:
            index = names.index(search_name)
            print(f"Employee: {search_name}, Salary: ${salaries[index]:,.2f}")
        else:
            print("Employee Not Found.")

display_employees(employee_names, employee_salaries)
display_employees_reverse(employee_names)
find_highest_salary(employee_names, employee_salaries)
sum_total_salary(employee_salaries)
search_employee(employee_names, employee_salaries)
