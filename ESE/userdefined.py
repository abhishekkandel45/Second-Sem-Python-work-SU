# User Defined Exception for Voters Elegibility Check:
class VotersEligibitiesError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise VotersEligibitiesError("You are not eligible to vote")
    else:
        print("You are eligible to vote")
except VotersEligibitiesError as e:
    print(e)
except ValueError:
    print("Invalid age")
except Exception as e:
    print("Something went wrong")
    print(e)
else:
    print("No exception")
finally:
    print ("Program completed")
    