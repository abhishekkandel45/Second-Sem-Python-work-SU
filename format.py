# write a program that ask user for theri full email address and and their 10 digit phone number and 
# print them in the following format:
# ================================
#               YOUR INFO
# ================================

# Enter email: 
# Enter phone number:

# ================================

# Domain: xxx.xxx
# User Name: xxxxxxx
# Phone Number: (xxx) xxx-xxxx

# ================================


#Code:
print("====================================================")
print("                    YOUR INFO")
print("====================================================")
c=input("Enter email: ")
d=input("Enter phone number: ")
print("====================================================")
print("Domain: ",c.split("@")[1])
print("User Name: ",c.split("@")[0])
print("Phone Number: (",d[0:3],")",d[3:6],"-",d[6:10])
print("====================================================")

