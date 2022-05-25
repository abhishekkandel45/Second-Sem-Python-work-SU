#To perform division by using try and except and finally blocks to handle the exception
# Sale calculator in Nepal Stock Exchange which includes the following criteria:
# Broker commission is 0.4% upto Rs.50000, 0.37% for  Rs. 500000 to Rs. 2000000, 0.30% for Rs. 2000000 to 10000000 and 0.27% above 10000000 total transaction amount
# Capital Gain tax is 7.5% of profit made if the invester holds the share for less than 1 year and 5% of profit made if the invester holds the share for more than 1 year
# DP charge is fixed for both personal and institutional investors and is Rs.25


numShares = int(input("Enter the number of shares: "))
ShareCode = input("Enter the share code: ")
BuyinPrice = float(input("Enter the buyin price: "))
SalePrice = float(input("Enter the sale price: "))

# Date input method and validation fuction
def date_input(date):
    try:
        date = datetime.datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        print("Please enter a valid date")
        date = input("Enter the date of purchase: ")
        date = date_input(date)
    return date

# Date Inputs are validated and converted to datetime format
DateofPurchase = date_input(DateofPurchase)
DateofSale = date_input(DateofSale)


#calculation of share ammount
ShareAmmount = BuyinPrice * numShares
print ("Share ammount: ", ShareAmmount)
#calculation of brocker commission
if ShareAmmount <= 50000:
    Commission = ShareAmmount * 0.004
elif ShareAmmount <= 500000:
    Commission = ShareAmmount * 0.037   
elif ShareAmmount <= 2000000:
    Commission = ShareAmmount * 0.30
elif ShareAmmount <= 10000000:
    Commission = ShareAmmount * 0.27
else:
    Commission = ShareAmmount * 0.27
print ("Brocker commission: ", Commission)

#profit loss calculation
ProfitLoss = SalePrice - BuyinPrice
print ("Profit/Loss: ", ProfitLoss)

#Capital gain tax calculation according to years of holding and profit loss
if DateofPurchase <= DateofSale:
    if DateofSale - DateofPurchase <= 365:
        CapitalGainTax = ProfitLoss * 0.075
    else:
        CapitalGainTax = ProfitLoss * 0.05
else:
    CapitalGainTax = 0
print ("Capital gain tax: ", CapitalGainTax)

#DP charge calculation
DPCharge = 25
print ("DP charge: ", DPCharge)

# Final Share Ammount
FinalShareAmmount = ShareAmmount - Commission - CapitalGainTax - DPCharge
print ("Final share ammount: ", FinalShareAmmount)

#Final profit and loss
FinalProfitLoss = FinalShareAmmount - ShareAmmount
print ("Final profit/loss: ", FinalProfitLoss)

#final Price per share
FinalPricePerShare = FinalShareAmmount / numShares
print ("Final price per share: ", FinalPricePerShare)
