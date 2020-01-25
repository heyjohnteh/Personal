
#generate random number
import random
number = random.randint(0 , 100)

#prompt user for input
guess = eval(input("guess a number between 0 and 100: "))

#setting feedback for different guesses
while True:
    if number == guess:
        print("Congrats you're correct!")
        break
    elif (guess >= 100) or (guess <= 0):
        print ("guess is not within range try again")
        guess = eval(input("guess a number between 0 and 100: "))
    elif (100 > guess > number):
        print ("guess is too high try again")
        guess = eval(input("guess a number between 0 and 100: "))
    elif (0 < guess < number):
        print ("guess is too low try again")
        guess = eval(input("guess a number between 0 and 100: "))
