# A simple python program to find the output of following programs.

print("\n[OutPut of PROGRAM 1]\n")
for i in range (20,30,2): print(i)

print("")

print("[OutPut of PROGRAM 2]\n")
country = "INDIA"
for i in country: print(i) 

print("")

print("[OutPut of PROGRAM 3]\n")
i = 0; sum = 0;
while i < 9:
    if i % 4 == 0:
        sum = sum + i
        i = i + 2
        print (sum)