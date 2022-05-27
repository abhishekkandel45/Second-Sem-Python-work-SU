#Q1. Define a function that prints a dictionary where the keys are numbers between 1 and 4 (both included) and the values are cubes of the keys.
#For example:
#{1: 1, 2: 8, 3: 27, 4: 64}

def gen_dict():
    d = {}
    for i in range(1,5):
        d[i] = i**3
    print (d)
gen_dict()