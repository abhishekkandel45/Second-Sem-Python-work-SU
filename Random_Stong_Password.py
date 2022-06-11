# Write a program to create a random storng password.
# The password should be a minimum of 8 characters long and should
# include at least one uppercase letter, one lowercase letter,
# one digit, and one special character.

import random
import string
passKey = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(passKey) for i in range(8))
print(password)
