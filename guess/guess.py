# import the random module
import random

# greeting
print("guess a number from 1 to 100")

# initial value
number = random.randint(1, 100)
# guess=int(input("take a guess"))
tries = 0

# loop & end when guess too much time
while tries < 6:
    guess = int(input("take a guess"))
    tries += 1
    if guess > number:
        print("lower the number, guess again")
    elif guess < number:
        print("higher the number, guess again")
    else:
        print("you got it! The number was", number)
        print("You only try", tries, "times")

if guess != number:
    print("Guess too much time, game over.")

# congrats


# end
