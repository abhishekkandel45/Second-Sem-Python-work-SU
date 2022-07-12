#Objectr oriented Programming in Python:
class Customer:
    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type
        print("membership created")

c= Customer("Abhishek", "Gold")
print(c.name, c.membership_type)

