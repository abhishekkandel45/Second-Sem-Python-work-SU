#Write a python program to show inheritance in python programming?
class Employee:
    pass
class FullTimeEmployee(Employee):
    pass
class PartTimeEmployee(Employee):
    pass

# Keeping the details of the employees:

# Full Time Employee:
fullTimeEmployee=FullTimeEmployee()
fullTimeEmployee.name=input("Enter the name of the employee: ")
fullTimeEmployee.age=int(input("Enter the age of the employee: "))
fullTimeEmployee.salary=int(input("Enter the salary of the employee: "))
print("The name of the employee is: ",fullTimeEmployee.name)
print("The age of the employee is: ",fullTimeEmployee.age)
print("The salary of the employee is: ",fullTimeEmployee.salary)

# Part Time Employee:
partTimeEmployee=PartTimeEmployee()
partTimeEmployee.name=input("Enter the name of the employee: ")
partTimeEmployee.age=int(input("Enter the age of the employee: "))
partTimeEmployee.salary=int(input("Enter the salary of the employee: "))
print("The name of the employee is: ",partTimeEmployee.name)
print("The age of the employee is: ",partTimeEmployee.age)
print("The salary of the employee is: ",partTimeEmployee.salary)
