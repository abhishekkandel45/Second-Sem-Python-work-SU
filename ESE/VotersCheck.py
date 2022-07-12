from re import L
from typing import final


class VotersCheck(Exception):
    pass
try:
    age=int(input("ENter the Age"))
    if age<18:
        raise VotersCheck(" You're Underage")
    else:
        print(" You're Eligible to Vote")
except VotersCheck as e:
    print (e)

except ValueError:
    print("invalid Age")

except Exception as e:
    print("Something went Wrong")
    print (e)
else:
    print(" no Exception Found")
finally:
    print("End of the program")
