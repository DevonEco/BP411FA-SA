#importing the random module
import random

#main program with user input
y = int(input("How many values must the list contain?: "))
#creating empty list
myList = []
for x in range(0,y):
    myList.append(random.randint(0,100))

#defining sumList()
def sumList():
    print(myList)
    listSum  = sum(myList)
    print("The total is: " + str(listSum))

#calling sumList()
sumList()
