#Demostrate Local and Global Variables.
#Local variables are variables that are declared inside a function.
#Global variables are variables that are declared outside a function.

#Program to demonstrate the use of Local and Global Variables.

global_var = 5                     #Global Variable
def add(a,b):
    local_var = a+b                #Local Variable
    print("The sum is",local_var)
    print("The global variable is",global_var)
add(10,20)