# Number-guesser
Python project 1
import random
while True:
    game = input("Do you want to guess (m) or shall I (y)?")
    if game == "m":
        print("I'm thinking of a number between 1 and 100.")
        secret_num = random.randint(1, 100)
        guess = 0
        attempts = 0
        while secret_num != guess:
            n= input("Guess a number between 1 and 100 ")
            guess = int(n)
            attempts += 1
            if secret_num < guess:
                print(f"{guess} is too high, Guess Lower ")
            elif secret_num > guess:
                print(f"{guess} is too low, Guess Higher ")
            else:
                print(f"You guessed the number {guess} in {attempts} attempts! well done!")
    if game == "y":
        y= input("Submit a number between 1 and 100: I will try and guess it ")
        my_num = int(y)
        high_bound = 100
        low_bound = 1
        attempts = 0
        guess = random.randint(1, 100)
        while True:
            me = input(f"My guess is {guess} is it too high (h) too low (l) or correct (c)?")
            attempts += 1
            if me == "h":
                if guess < high_bound:
                    high_bound = guess-1
                else:
                    guess = random.randint(low_bound, high_bound)
            elif me == "l":
                if guess > low_bound:
                    low_bound = guess+1
                else:
                    guess = random.randint(low_bound, high_bound)
            elif me == "c":
                if guess == my_num:
                    print(f"I guessed the number {guess} in {attempts} attempts!")
                else:
                    print(f"You said correct but my number doesn't match, is it higher (h) or lower (l)?")
                break
            else:
                print(f"Sorry, I don't understand {me}")
                attempts = -1
    print("Game Over")
    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again != 'yes':
        break

print("Thanks for playing!")
