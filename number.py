import random

def select_difficulty() -> int:
    """Позволяет игроку выбрать уровень сложности и возвращает количество попыток."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")
    print("Please select the difficulty level: ")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Great! You selected Easy.\n")
                return 10
            elif choice == 2:
                print("Great! You selected Medium.\n")
                return 5
            elif choice == 3:
                print("Great! You selected Hard.\n")
                return 3
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game(tries: int):
    """Основная игра угадай число."""
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while tries > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1
        tries -= 1

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            return
        elif guess < number_to_guess:
            print(f"Too low! You have {tries} tries left.\n")
        else:
            print(f"Too high! You have {tries} tries left.\n")

    print(f"😢 Game Over! The number was {number_to_guess}.")

if __name__ == "__main__":
    total_tries = select_difficulty()
    play_game(total_tries)
