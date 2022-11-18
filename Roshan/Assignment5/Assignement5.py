
 
# Code Starts Here
# Format the table
print("Birthday Money Inc.")
print("===================")
print()
print("Welcome to Birthday Money Inc.! We mail birthday money, so you don't have to!")
print()
print("Only a $0.50 fee per recipient.")
print()
print("Enter 3 recipients' information below.")
print()
print("-----------------------------------------------------------------------------")
print()

# Ask for the first name, last name, and age of the for 3 recipients and them in list
first_name = []
last_name = []
age = []
for i in range(3):
    first_name.append(input("Enter first name: "))
    last_name.append(input("Enter last name: "))
    age.append(input("Enter age: "))
    print()

# Print the table
print("Order Information")
print("=================")
print()
print("+------------------+------------------+-----+-----------+")
print("|    Last  Name    |    First Name    | Age |   Money   |")
print("+------------------+------------------+-----+-----------+")
for i in range(3):
    print("| {:<16} | {:<16} | {:<3} | ${:<9.2f} |".format(last_name[i], first_name[i], age[i], float(age[i])))
    print("+------------------+------------------+-----+-----------+")
print()

# Calculate the subtotal, tax, and total
subtotal = 0
for i in range(3):
    subtotal += float(age[i])
subtotal += 1.5
tax = subtotal * 0.11
total = subtotal + tax

# Print the receipt
print("Receipt")
print("=======")
print()
print("Subtotal      ${:<8.2f}".format(subtotal))
print("Tax           ${:<8.2f}".format(tax))
print("----------------------")
print("Total         ${:<8.2f}".format(total))
print()

# Code Ends Here

 
 
