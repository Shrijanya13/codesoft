import random

# Function to get the computer's random choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to display the scores
def display_scores(user_score, computer_score):
    print(f"User Score: {user_score} | Computer Score: {computer_score}")

# Main game loop
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("Choose rock, paper, or scissors (or type 'quit' to stop): ").lower()
        if user_choice not in ["rock", "paper", "scissors", "quit"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        if user_choice == "quit":
            print("Thanks for playing!")
            break

        # Computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update score
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display scores
        display_scores(user_score, computer_score)

        # Ask if user wants to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Game over!")
            break

if __name__ == "__main__":
    play_game()
