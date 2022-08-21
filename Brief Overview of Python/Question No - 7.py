# A simple python program to repeat the string "Good Morning" n times.

nTimes = int(input("How many times you want me to wish [Good Morning]: ")) #Gets the n times of number.

counter = 1 #Starts a counter that counts the Good Morning messages printed yet.

while nTimes >= counter: #while loop to run until counter equals the nTimes number.
    print("Good Morning.") #prints the good morning message.
    counter = counter + 1 #Incerase the counter value to 1
