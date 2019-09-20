##### ADAM MANSURI

import random
import time

##### these 3 lines of code will generate our random suit for each player:
suits = ["Hearts","Spades","Clubs","Diamonds"]
player1suit = random.choice(suits)
player2suit = random.choice(suits)

##### player 1 random card number:
player1card1 = random.randint(1,13)
player1card2 = random.randint(1,13)
player1card3 = random.randint(1,13)

##### player 2 random card number:
player2card1 = random.randint(1,13)
player2card2 = random.randint(1,13)
player2card3 = random.randint(1,13)

##### player 1 max value:
maxValue1= max(player1card1,player1card2,player1card3)

##### player 2 max value:
maxValue2= max(player2card1,player2card2,player2card3)

##### player 1 - sum of 3 values:
player1sum = player1card1+player1card2+player1card3

##### player 2 - sum of 3 values:
player2sum = player2card1+player2card2+player2card3


print("Lets Begin The Game!")
print("")


##### FOR PLAYER 1

player1 = input("Player 1, Please enter your name: ")
print("") ##### this is to create a space between lines of code - for a better layout
print(player1)
time.sleep(1.5)  ##### this is to give pauses, making it feel more like a game

print("Your numbers are:")
time.sleep(1.5)

print(player1card1,player1card2,player1card3)


time.sleep(1.5)
print(player1, "Your highest value is", maxValue1,"of",player1suit)
time.sleep(2.2)

if maxValue1 == 11:
    print("Your highest card is a Jack")
elif maxValue1 == 12:
    print("Your highest card is a Queen")
elif maxValue1 == 13:
    print("Your highest card is a King")
elif maxValue1 == 1:
    print("Your highest card is an Ace")
else: print("Your highest card is", maxValue1)
time.sleep(2.5)

print("")

##### FOR PLAYER 2
player2 = input("Player 2, Please enter your name: ")
print("")
print(player2)
time.sleep(1.5)

print("Your numbers are:")
time.sleep(1.5)

print(player2card1,player2card2,player2card3)


time.sleep(1.5)
print(player2, "Your highest value is", maxValue2,"of",player2suit)
time.sleep(2.2)


if maxValue2 == 11:
    print("Your highest card is a Jack")
elif maxValue2 == 12:
    print("Your highest card is a Queen")
elif maxValue2 == 13:
    print("Your highest card is a King")
elif maxValue2 == 1:
    print("Your highest card is an Ace")
else: print("Your highest card is", maxValue2)
time.sleep(2.5)

print("")

if maxValue1>maxValue2:
    print(player1, " you have the highest value of", maxValue1)

elif maxValue1<maxValue2:
    print(player2, " you have the highest value of", maxValue2)

else:
    print("You both have the same highest value, which is", maxValue1)
print("")
time.sleep(2.5)
##### GAME OVER - FINAL SCORE - WIN/DRAW
print("Now, lets see who the overall winner is...")
time.sleep(3)
print("")

print(player1,"- the sum of your cards is",player1sum)
time.sleep(2.5)
print(player2,"- the sum of your cards is",player2sum)
print("")
time.sleep(2.5)

if player1sum>player2sum:
    print("Congratulations", player1,"You have won!")
elif player2sum>player1sum:
    print("Congratulations", player2,"You have won!")
else:
    print("Its a draw!")

time.sleep(10)
