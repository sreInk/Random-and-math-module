import random
w = True
number = str(random.randint(110,115))

print("Guess the game for 1 lakh rs")
while w:
    guess = input("Enter NUmber Between 110 TO 115")
    if guess==number:
     print("1 LAKH Sent To Your Bank Account")
     break
    else:
     print("You lose do not put money on this webpage")