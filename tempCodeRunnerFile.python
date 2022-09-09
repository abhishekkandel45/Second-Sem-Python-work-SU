#Condition:
# Age <==2 : No Charge
# Age >=3 and Age <=12 : $ 15
# Age >=13 and Age <=60 : $ 20
# Age >=61 : $ 18
# Create a program that begin with reading the age of the user, with one age entered on each line.
# The user will enter blank line to indicate that there are no visitors in the group.
# The program will then print the total amount of money that the group will have to pay.

age=[]
total=0
while True:
    a=input("Enter age: ")
    if a=="":
        break
    age.append(int(a))
for i in age:
    if i<3:
        total+=0
    elif i<13:
        total+=15
    elif i<61:
        total+=20
    else:
        total+=18
#printing with 2 decimal places format
print("Total: $",format(total,".2f"))