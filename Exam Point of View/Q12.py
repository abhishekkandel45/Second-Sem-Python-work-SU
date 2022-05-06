# Write a python program to accept a name from the user and verify whether the name is authorized or not?
# The name should be in the list of authorized names.
a=input("Enter a name: ")
b=["John","Mary","Bob","Alice"]
if a in b:
    print ("Authorized")
else:
    print ("Unauthorized")
