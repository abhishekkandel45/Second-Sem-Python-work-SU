# Demostrate a python  to print try, expect and  finally blocks in a program
a= (int(input("Enter the number")))5
try:
    if a<0:
        raise ValueError
    else:
        print(a)
except ValueError:
    print("Enter a positive number")
finally:
    print("Thank you")
