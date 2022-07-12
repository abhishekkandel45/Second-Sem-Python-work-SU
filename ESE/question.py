#If ATM contains Indian currency notes of 100, 500, and 2000. To withdraw cash from 
# ATM, the user has to enter number of notes he/she wants of each currency i.e. of 100, 
# 500 and 2000. So write a program calculate total amount withdrawn by person from 
# ATM in terms of rupees.

n=int(input("Enter the number of notes of 100: "))
m=int(input("Enter the number of notes of 500: "))
o=int(input("Enter the number of notes of 2000: "))
print("Total amount withdrawn by you is: ",(n*100)+(m*500)+(o*2000))
