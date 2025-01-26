# 3. Number Guessing Game

def numberGuessingGame():
    import random
    number = random.randint(1, 100)
    while True:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("Congratulations! You guessed the number.")
            break
        elif guess < number:
            print("Too Low")
        else:
            print("Too High")
            break
numberGuessingGame()
