# Write a program to enter names of the Employees and their salaries as input and store them in a dictionary.
a=int(input("Enter the number of employees: "))
b={}
for i in range(a):
    c=input("Enter the name of the employee: ")
    d=int(input("Enter the salary of the employee: "))
    b[c]=d
print (b)