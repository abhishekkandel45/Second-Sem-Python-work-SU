#Catching Exceptions:

randomlist = [1,2,3,4,5,6,7,8,9,10]
try:
    print (randomlist[11])
except IndexError:
    print ("Index out of range")
except:
    print ("Unexpected error:" )