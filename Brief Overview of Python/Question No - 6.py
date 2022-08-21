# A simple python program to calculate the amount payable if money has been lent on simple interest. 

PmoneyLent = float(input("Principle Money Lent: ")) #Gets Principle amount money lent by the user.

ratePercent = float(input("Simple Interest Rate Per annum(in %): ")) #Gets Rate per annum from the user.

Time = int(input("Time(in years): ")) #Gets time for which period money is to be repaid.
print("") #Vacant SPace to look good.

sInterest = float((PmoneyLent * ratePercent * Time)/100) #Calculates Simple Interest.
                                                         #Simple Interest = (P x R x T)/ 100. 

amountPayable = PmoneyLent + sInterest #Calculates amount payable by the user. 
                                       ## Amount payable = Principal + SI.

print("Amount Payable = "+ str(amountPayable))
