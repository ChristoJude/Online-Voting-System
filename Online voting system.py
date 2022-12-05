print("------------------------------------------------------------")
print("             ONLINE VOTING SYSTEM             ")
print("            ----------------------")
numofvoter = int(input("Enter the total number of voters:"))
print(numofvoter)
i = 0
list1 = []
list2 = []
for i in range(1, numofvoter + 1):
    print("----------------------------------------")
    print("Who would you like to vote for?")
    print(" ")
    print("1. Person1")
    print(" ")
    print("2. Person2")
    print(" ")
    a = int(input("Enter the Option(1/2):"))
    print("----------------------------------------")
    print(a)
    print("----------------------------------------")
    if a == 1:
        list1.append([i])
    elif a == 2:
        list2.append([i])
    else:
        print("Wrong Option")
        break
result = input("Would you like to view the results(y/n):")
if result == 'y':
    print("----------------------------------------")
    print(" ")
    print("Total votes for Person1 is:", len(list1))
    print(" ")
    print("Total votes for Person2 is:", len(list2))
    print("----------------------------------------")
else:
    print("----------------------------------------")
    print("Thank you for using my Online voting system")
    print("----------------------------------------")
