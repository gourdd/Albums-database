# Lists

food = ["pizza", "hamburger", "hotdog", "spaghetti"]

print(food)

print(food[3])

# Index out of range error:
try:
    print(food[4])
except IndexError as e:
    print("out of bounds")

food[0] = "sushi"

print(food[0])

# Lists are dynamic when you do food.append

print()
print(food)
print("Appending the food 'Salmon' to food list")
food.append('Salmon')
print(food)

# Testing for aka list:
print()
print("Testing for aka list:")
akaList2 = []
print(akaList2)

testLock = 0
listCounter = 0

# try again

# Aka list simulation:
foodList = []

loopLock = 0
itemCounter = 1
while loopLock == 0:

    foodInput = input("Add item #"+str(itemCounter)+" to the foodList: ")
    foodList.append(foodInput)
    itemCounter +=1

    try:
        stayInLock = 0
        
        while stayInLock == 0:
            stayIn = int(input("Would you like to add another? 1 for yes 2 for no: "))

            if stayIn == 2:
                loopLock = 1
                stayInLock = 1
            else:
                if stayIn != 1:
                    print("Invalid input. Please enter again.")
                else:
                    stayInLock = 1

    except ValueError as e:
        print("Invalid input. Please enter again.")
print(foodList)