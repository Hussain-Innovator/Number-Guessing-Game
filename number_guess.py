import random

def number_guessing_game():
    print("\n🎯 Welcome to the Number Guessing Game! 🎯\n")
    
    # Step 1: Allow user to set a custom range
    min_val = int(input("Enter the minimum number: "))
    max_val = int(input("Enter the maximum number: "))
    
    if min_val >= max_val:
        print("⚠️ Invalid range! Setting default range 1 to 100.")
        min_val, max_val = 1, 100

    # Step 2: Generate a random number within the range
    secret_number = random.randint(min_val, max_val)

    # Step 3: Let the user select difficulty level
    print("\nSelect Difficulty Level:")
    print("1️⃣ Easy (10 attempts)")
    print("2️⃣ Medium (7 attempts)")
    print("3️⃣ Hard (5 attempts)")
    
    level = input("Enter your choice (1/2/3): ")
    attempts_left = {"1": 10, "2": 7, "3": 5}.get(level, 10)  # Default is 10 attempts
    
    print(f"\n🔢 A secret number has been chosen between {min_val} and {max_val}. Try to guess it!")

    # Step 4: Start the guessing loop
    attempts = 0
    while attempts_left > 0:
        try:
            guess = int(input("\nYour guess: "))  # User input
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

        attempts += 1
        attempts_left -= 1

        # Step 5: Check the guess
        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break
        
        print(f"⚡ Attempts left: {attempts_left}")

    # Step 6: If attempts run out, reveal the number
    if attempts_left == 0:
        print(f"❌ Game Over! The correct number was {secret_number}.")

    # Step 7: Ask user if they want to play again
    restart = input("\n🔄 Do you want to play again? (yes/no): ").lower()
    if restart == "yes":
        number_guessing_game()
    else:
        print("👋 Thanks for playing! See you next time.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
