# A simple python program to understand the difference b/w else & elif statement.


print("\nASSUMING You have applied for a driving license.\n")
print("Age is greater than 18 or equal to 18 - Eligible for Driver's License [IF]")
print("Age is less than 18 but greater than 15 - Eligible for Learning Driver's License only [ELIF]")
print("Age is less than 15 - NOT Eligible for any driving license [ELSE]\n")

ageUser = int(input("Enter Your Age: "))

if ageUser >= 18: #Firstly this condition executes.
    print("Eligible for Driver's License")

elif ageUser < 18 and ageUser > 15: #If First COndition fails then this executes.
    print("Eligible for Learning Driver's License")

else : print("NOT Eligible for any driving license.") #If all the conditions fails then this executes ar last.

print("\nCheck Source Code of this program to understand mor deeply the difference b/w elif and else.")

