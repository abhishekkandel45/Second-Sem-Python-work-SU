#Simple Cal
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
ch=int(input("Enter your choice(1/2/3/4/5) "))
if ch==1:
    print(a+b)
elif ch==2:
    print(a-b)
elif ch==3:
    print(a*b)
elif ch==4:
    print(a/b)
elif ch==5:
    print("Thank you")
else:
    print("Invalid choice")
    print("Thank you")