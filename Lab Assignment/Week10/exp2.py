# Write a program to demosntrate inheritance in python. it should keep students Detail.
class Student:
    pass
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("The name of the student is: ",self.name)
        print("The age of the student is: ",self.age)
        print("The marks of the student is: ",self.marks)