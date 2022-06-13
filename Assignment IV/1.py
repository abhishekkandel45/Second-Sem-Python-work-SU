# What is self keyword explain with an example?
# self is a reference to the current instance of the class.

# Example to demonstrate the use of self keyword in a class which should take input from the user and print the output.
class Student:
    def __init__(self, name, age, rollno):
        self.name = input("Enter the name: ")
        self.age = input("Enter the age: ")
        self.rollno = input("Enter the rollno: ")
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Rollno: ", self.rollno)

#INPUT
s1 = Student("", "", "")
#OUTPUT
s1.display()
