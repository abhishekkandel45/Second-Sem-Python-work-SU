#write a program that calculates the tip that will be added to the  final cost of a meal at a restaurant based on customer satisfaction. 
#First, ask the user to enter the total cost. Next, display the rating system for their experience, and ask them to enter their rating as 1,
# 2, or 3. Based on the rating, calculate the correct tip. The tip is calculated as follows:
# 20% tip for totally satisfied
# 15% for satisfied
# 10% for dissatisfied
# Finally, display the tip and final total.

#Test CASES
#As you write your program, you will need to test it, especially your decision structures. Download the Test Cases file from Moodle and fill in 
# each row with the results of the tests in the file. It doesn’t  matter if the test is successful or not; the point is to document the testing
#  process.



# SSAMPLE OUTPUT

# ================================================
#                   CHECKOUT
# ================================================
#
#  ENTER THE TOTAL COST : 100
#
# =================================================
#                      RATING
# =================================================
#    +-----------------------------------+
#    |       RATE YOUR EXPERIENCE !      |
#    |     __________________________    |
#    |     1=TOTALLY SATISFIED           |
#    |     2=SATISFIED                   |
#    |     3=DISSATISFIED                |
#    +-----------------------------------+
# ENTER YOUR RATING : 1
#
# =================================================
#                      PAYMENT
# =================================================
#
#  TIP :            20.0
#  TOTAL :          120.0
#
# =================================================


#Solution
print ("===============================================")
print ("                  CHECKOUT")
print ("===============================================")
print ("")
total = float(input("ENTER THE TOTAL COST : "))
print ("")
print ("=================================================")
print ("                     RATING")
print ("=================================================")
print ("   +-----------------------------------+")
print ("   |       RATE YOUR EXPERIENCE !      |")
print ("   |     __________________________    |")
print ("   |     1=TOTALLY SATISFIED           |")
print ("   |     2=SATISFIED                   |")
print ("   |     3=DISSATISFIED                |")
print ("   +-----------------------------------+")
rating = int(input("ENTER YOUR RATING : "))
print ("")
print ("=================================================")
print ("                     PAYMENT")
print ("=================================================")
print ("")
if rating == 1:
    tip = total * 0.2
    #Formating the out with 2 decimal places
    print (" TIP :            {0:.2f}".format(tip))
    print (" TOTAL :          {0:.2f}".format(total + tip))
elif rating == 2:
    tip = total * 0.15
    print (" TIP :            {0:.2f}".format(tip))
    print (" TOTAL :          {0:.2f}".format(total + tip))
elif rating == 3:
    tip = total * 0.1
    print (" TIP :            {0:.2f}".format(tip))
    print (" TOTAL :          {0:.2f}".format(total + tip))
else:
    print (" INVALID RATING !")

#Printing the lower line
print ("")
print ("=================================================")

