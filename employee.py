def show_employee():
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    if salary >= 20000:
        print("Your name is: ", name + " " + "and your salary is: ", salary)
    else:
        print("You do not qualify for company loan")


show_employee()

