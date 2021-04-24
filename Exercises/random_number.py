import random

RAND_NUM= random.randint(1,100)

Guess=5
keep_playing = True

while keep_playing:
    userGuess=int(input("Enter a number between 0 and 100: "))
    Guess-=1
    if userGuess>100:
        print("Guess number should not be more than 100")
        break
    if userGuess<RAND_NUM:
        print("Guess number is low")
    elif userGuess>RAND_NUM:
        print("Guess is too high")
    elif userGuess==RAND_NUM:
        print("Your guess the number "+ str(RAND_NUM)+ "is right")
    if Guess==0:
        print("You ran out of guesses")
        print("Random number is "+ str(RAND_NUM))
        keep_playing = False