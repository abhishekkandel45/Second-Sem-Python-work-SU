# Create a dictionary "ODD" of odd number between 1 and 10, where the key key is the number and the value is the cross product of the number and the number in words.
#Perform the Following operations on the dictionary:
# Diplay the Keys
# Display the Values
# Dispaly the item
# Find the length of the dictionary
#check if 7 is present in the dictionary
# Check 2 is present in the dictionary
# Retrive the value crossponding to the key 9
# Delete the Item from the dictionary crossponding to the key 9

Key = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
print(Key)
print(Key.keys())
print(Key.values())
print(Key.items())
print(len(Key))
print(Key.get(7))
print(Key.get(2))
print(Key.pop(9))
print(Key.remove(9))