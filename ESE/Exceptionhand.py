a= int(input("Enter the Number:"))
b= int(input("Enter the number:  "))
try:
    print (a/b)
except ZeroDivisionError:
    print(" Cannot Devide by Zero")

except ValueError:
    print ("Invalid Input")

except Exception as e:
    print("Something went wrong", e)
finally:
    print("Program Executed successfully")
