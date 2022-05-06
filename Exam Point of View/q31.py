# Write a python program to find the Volume of Shapes?
print ("Enter the shape you want to find the volume of: ")
print ("1. Sphere")
print ("2. Cylinder")
print ("3. Cone")
print ("4. Cube")
print ("5. Rectangular Prism")
print ("6. Pyramid")
print ("7. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    r = int(input("Enter the radius: "))
    volume = 4/3*3.14*r**3
    print ("The volume of the sphere is: ", volume)
elif choice == 2:
    r = int(input("Enter the radius: "))
    h = int(input("Enter the height: "))
    volume = 3.14*r**2*h
    print ("The volume of the cylinder is: ", volume)
elif choice == 3:
    r = int(input("Enter the radius: "))
    h = int(input("Enter the height: "))
    volume = 1/3*3.14*r**2*h
    print ("The volume of the cone is: ", volume)
elif choice == 4:
    l = int(input("Enter the length: "))
    volume = l**3
    print ("The volume of the cube is: ", volume)
elif choice == 5:
    l = int(input("Enter the length: "))
    w = int(input("Enter the width: "))
    h = int(input("Enter the height: "))
    volume = l*w*h
    print ("The volume of the rectangular prism is: ", volume)
elif choice == 6:
    b = int(input("Enter the base: "))
    h = int(input("Enter the height: "))
    volume = 1/3*b*h
    print ("The volume of the pyramid is: ", volume)
elif choice == 7:
    print ("Thank you for using the Volume Calculator")
    exit()
else:
    print ("Invalid choice")
print ("Thank you for using the Volume Calculator")
