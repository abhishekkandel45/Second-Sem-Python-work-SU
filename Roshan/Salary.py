# Write a Python program to calculate employee bonus and display the results on the screen. 
#First your program read employee name, service and salary amount.
#Then compute the BONUS as follows:
#• If SERVICE is less than 5 years, give YEARLY BONUS 2 times of his/her MONTHLY SALARY.
#• If SERVICE is between 5 and 10 (less than 10), give YEARLY BONUS 3 times of his/her MONTHLY SALARY.
#• If SERVICE is equal or more than 10 years, give YEARLY BONUS 3.5 times of his/her
#MONTHLY SALARY.
#Sample output would be as follows:

#                   ALPHA CO. LTD.
#           TABLE OF BONUS IN DEC. 2021
#
# NO.  NAME        SERVICE   SALARY   BONUS
#-------------------------------------------
#1   MR. SAM        10        10000     35000
#2   MR. JOHN       8         12000     36000
#3   MR. JAN        3         8000      16000
#4   MR. PAN        12        5000      17500
#5   ........      ....      ....      ....

# The Final output should be displayed on the screen at the end of the program.

#Taking input from user (No of employees)
n = int(input("Enter the number of employees: "))
#Creating a list of lists to store the data
data = []
#Taking input from user (Employee name, service and salary)
for i in range(n):
    name = input("Enter the name of employee: ")
    service = int(input("Enter the service of employee: "))
    salary = int(input("Enter the salary of employee: "))
    data.append([name, service, salary])
#Calculating the bonus
for i in range(n):
    if data[i][1] < 5:
        bonus = data[i][2] * 2
    elif data[i][1] >= 5 and data[i][1] < 10:
        bonus = data[i][2] * 3
    else:
        bonus = data[i][2] * 3.5
    data[i].append(bonus)
#Printing the data
print("                  ALPHA CO. LTD.")
print("          TABLE OF BONUS IN DEC. 2021 ")
print(" NO.  NAME        SERVICE   SALARY   BONUS")
print("-------------------------------------------")
for i in range(n):
    #Printing the data in a tabular format using string formatting with Salutation
    print("{0:3}  MR. {1:10} {2:8} {3:8} {4:8}".format(i+1, data[i][0], data[i][1], data[i][2], data[i][3]))
    