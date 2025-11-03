from askii import art,gameOver, youWin
print(art)
print("Welcome to treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('You\'re at a crossroad, where do you want to go? Type "left" ot "right". ').lower()
if choice1 == "left":
    choice2=input('You\'ve come to the lake. There\'s an island in the middle of the lake. '
     'Type "wait" to wait for a boat. ' 
     'Type "swim" to swimm across. ').lower()
    if choice2 == "wait":
        choice3 = input('You arrived at the island unharmed.There is a house with 3 doors. '
        'One red, one blue and one yellow. Which colour do you choose? ').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over")
            print(gameOver)
        elif choice3 == "yellow":
            print("You found the treasure. You win")
            print(youWin)
        elif choice3== "blue":
            print("It's a room full of snakes. Game over.")
            print(gameOver)
        else: 
            print("You chose the door that doesn't exist. Game over")
            print(gameOver)  
    else:
        print("You got attacked by an angry trout. Game over.")
        print(gameOver)

    
else:
    print("You fell into the hole. Game Over")
    print(gameOver)
    

