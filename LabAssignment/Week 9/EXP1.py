num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter a valid number")
except:
    print("Something went wrong")
else:
    print("Success")
finally:
    print("Program completed")
print("End of program")
