# Write a program to demosntrate inheritance in python. it should keep students Detail.
class Student:
    pass
class StudentDetail(Student):
    pass
stuDetail=StudentDetail()
stuDetail.name=input("Enter the name of the student: ")
stuDetail.age=int(input("Enter the age of the student: "))
stuDetail.marks=int(input("Enter the marks of the student: "))
print("The name of the student is: ",stuDetail.name)
print("The age of the student is: ",stuDetail.age)
print("The marks of the student is: ",stuDetail.marks)