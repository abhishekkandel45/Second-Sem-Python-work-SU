#Design a function using polymorphism concept in Python to calculate area of an object.  The object may be a circle, rectangle or triangle
# and the function should return the area of the object.



def area(object,radius,length,breadth):
    if object=="circle":
        return 3.14*radius**2
    elif object=="rectangle":
        return length*breadth
    elif object=="triangle":
        return (length*breadth)/2
    else:
        return "Invalid object"

# Chosing the object
object=input("Enter the object: ")
if object=="circle":
    radius=int(input("Enter the radius: "))
    print("Area of the circle is: ",area(object,radius,0,0))
elif object=="rectangle":
    length=int(input("Enter the length: "))
    breadth=int(input("Enter the breadth: "))
    print("Area of the rectangle is: ",area(object,0,length,breadth))
elif object=="triangle":
    length=int(input("Enter the length: "))
    breadth=int(input("Enter the breadth: "))
    print("Area of the triangle is: ",area(object,0,length,breadth))
else:
    print("Invalid object")
    