import random

def guess_game():
    print("Welcome to the Number Guessing Game!")
    while True:
        number_to_guess = random.randint(1, 50)
        attempts = 0
        guessed = False

        print("\nI have selected a number between 1 and 50. Can you guess it?")

        while not guessed:
                user_guess = int(input("Enter your guess: "))
                attempts += 1

                if user_guess < 1 or user_guess > 50:
                    print("Please guess a number within the range 1-50.")
                    continue

                if user_guess < number_to_guess:
                    print("Too low!")
                elif user_guess > number_to_guess:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed it right.434")
                    print(f"You guessed it in {attempts} attempts.")
                    guessed = True
                    
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break
guess_game()   
