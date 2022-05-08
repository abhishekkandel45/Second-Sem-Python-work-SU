
# Wite a program to create a menu with the following options:
# 1. Area of a circle
# 2. Area of a rectangle
# 3. Area of a triangle
# 4. Area of a square
# 5. Area of a pyramid

# Accepts user inputs and perform the operation accordingly. Use Functions with arguements and return values.
from secrets import choice


print ("Welcome to the Area Calculator")
print ("1. Area of a circle")
print ("2. Area of a rectangle")
print ("3. Area of a triangle")
print ("4. Area of a square")
print ("5. Area of a pyramid")
print ("6. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14*radius**2
    print ("The area of the circle is: ", area)
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length*width
    print ("The area of the rectangle is: ", area)
elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = base*height/2
    print ("The area of the triangle is: ", area)
elif choice == 4:
    side = float(input("Enter the side of the square: "))
    area = side**2
    print ("The area of the square is: ", area)
elif choice == 5:
    base = float(input("Enter the base of the pyramid: "))
    height = float(input("Enter the height of the pyramid: "))
    area = base*height/3
    print ("The area of the pyramid is: ", area)
elif choice == 6:
    print ("Thank you for using the Area Calculator")
    exit()
else:
    print ("Invalid choice")
print ("Thank you for using the Area Calculator")
exit()
