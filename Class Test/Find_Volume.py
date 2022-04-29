#Wite a Python Program to find the volume of different Shapes
from secrets import choice


print ("1. Cube")
print ("2. Cylinder")
print ("3. Sphere")
print ("4. Cone")
print ("5. Exit")
a=int(input("Enter your choice: "))
if a==1:
    print ("1. Cube")
    print ("2. Exit")
    b=int(input("Enter your choice: "))
    if b==1:
        print ("Enter the length of the side of the cube: ")
        c=int(input())
        print ("The volume of the cube is: ",c**3)
    elif b==2:
        print ("Thank you for using the program")
    else:
        print ("Invalid choice")
elif a==2:
    print ("1. Cylinder")
    print ("2. Exit")
    b=int(input("Enter your choice: "))
    if b==1:
        print ("Enter the radius of the cylinder: ")
        c=int(input())
        print ("Enter the height of the cylinder: ")
        d=int(input())
        print ("The volume of the cylinder is: ",3.14*c**2*d)
    elif b==2:
        print ("Thank you for using the program")
    else:
        print ("Invalid choice")
elif a==3:
    print ("1. Sphere")
    print ("2. Exit")
    b=int(input("Enter your choice: "))
    if b==1:
        print ("Enter the radius of the sphere: ")
        c=int(input())
        print ("The volume of the sphere is: ",4/3*3.14*c**3)
    elif b==2:
        print ("Thank you for using the program")
    else:
        print ("Invalid choice")
elif a==4:
    print ("1. Cone")
    print ("2. Exit")
    b=int(input("Enter your choice: "))
    if b==1:
        print ("Enter the radius of the cone: ")
        c=int(input())
        print ("Enter the height of the cone: ")
        d=int(input())
        print ("The volume of the cone is: ",3.14*c**2*d/3)
    elif b==2:
        print ("Thank you for using the program")
    else:
        print ("Invalid choice")
elif a==5:
    print ("Thank you for using the program")
else:
    print ("Invalid choice")
    
