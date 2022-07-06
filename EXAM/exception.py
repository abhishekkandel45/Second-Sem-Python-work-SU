from decimal import DivisionByZero


a=int(input("ENter the firtst Number:"))
b=int(input("ENter the secomd number:"))
try:
    print (a/b)
except ZeroDivisionError:
    print ("Division by Zero is not allowed")
except ValueError:
    print ("Please Enter the valid number")
except:
    print("Something went wrong")
else: 
    print("Success")
finally:
    print(" Program Successful")   