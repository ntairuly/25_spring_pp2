from random import *
def Guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    number_guess = 0
    guesses=0
    while number_guess != number:
        guesses+=1
        print("Take a guess.")
        number_guess=int(input())
        print(" ")
        if number_guess > 20 or number_guess<1:
            print("This number is out of range ")
        elif number_guess>number :
            print("Your guess is too high.")
        elif number_guess<number:
            print("Your guess is too low.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
Guess_the_number()