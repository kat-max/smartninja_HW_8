secret = 29
guess = None

while secret != guess:
    guess = int(input("Guess a number: "))
    if guess == secret:
        print("Congrats! You have guessed the number!")
        break
    else:
        print("Wrong! Try your luck again!")
