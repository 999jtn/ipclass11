myList=[22,4,16,38,13]
choice=0
for attempt in range(3):print("Attempt number:", attempt)
print("The list 'myList' has the following element", myList)
print("L I S T  O P E R A T I O N S")
print(" 1. Append an element")
print(" 2. Insert an element at the desired position")
print(" 3. Append a list to the given list")
print(" 4. Modify an existing element")
print(" 5. Delete an existing element by its position")
print(" 6. Delete an existing element by its value")
print(" 7. Sort the list in ascending order")
print(" 8. Sort the list in descending order")
print(" 9. Display the list")
choice=int(input("Enter Your Choice (1-9): "))

if choice == 1:
    element = eval(input("Enter the element to be appended: "))
    myList.append(element)
    print("The element has been appended/n")

elif choice == 2:
    element = eval (input("Enter the element to be inserted: "))
    pos = int(input("Enter the position: "))
    myList.insert(pos,element)
    print("The element has been inserted/n")

elif choice == 3:
    newlist = eval(input("Enter the list to be appended: "))
    myList.extend(newlist)
    print("The list has been appended/n:")

elif choice  == 4:
    i = int(input("Enter the postion of the element to be modified: "))
    if i < len(myList):
        newElement = eval(input("Enter the new element: "))
        oldElement = myList[i]
        myList[i] = newElement
        print("The element",oldElement,"has been modified/n")
    else : 
            print("Position of the element is more then the lenght of list")

elif choice == 5:
    i = int(input("Enter the position of the element to be deleted: "))
    if i < len(myList):
        element = myList.pop(i)
        print("The element",element,"has been deleted/n")
    else :
            print("/nPosition of the element is more then the lenght of list")

elif choice == 6:
    element = int(input("Enter the element to be deleted: "))
    if element in myList:
        myList.remove(element)
        print("/nThe element",element,"has been deleted/n")
    else : 
            print("/nThe element",element,"is not persent in the list")

elif choice == 7:
    myList.sort()
    print("/nThe list has been sorted")

elif choice == 8:
    myList.sort(reverse = True) 
    print("/nThe list has been sorted in reverse order")

elif choice == 9:
    print("/nThe list is:", myList)
else : 
        print ("Choice is not valid")

