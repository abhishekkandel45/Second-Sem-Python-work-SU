# Q2. Write a program to find sum of two numbers using class and methods?
class Sum:
    def __init__(self,a,b):
        self.a=a=int(input("Enter first number: "))
        self.b=b=int(input("Enter second number: "))
    def sum(self):
        return self.a+self.b
s=Sum(0,0)      # creating object of class Sum
print("Sum of two numbers is: ",s.sum())
