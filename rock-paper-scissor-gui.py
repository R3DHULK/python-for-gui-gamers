import tkinter as tk
from random import choice

# Define choices
choices = ["rock", "paper", "scissors"]

# Define function to generate computer's choice


def computer_choice():
    return choice(choices)

# Define function to check winner


def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "User"
    elif user_choice == "paper" and computer_choice == "rock":
        return "User"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "User"
    else:
        return "Computer"

# Define function to play game


def play_game(user_choice):
    # Get computer's choice
    computer = computer_choice()

    # Check winner
    winner = check_winner(user_choice, computer)

    # Update result label
    if winner == "User":
        result_label.config(text="You win!")
    elif winner == "Computer":
        result_label.config(text="Computer wins!")
    else:
        result_label.config(text="Tie game!")

    # Update choices label
    choices_label.config(
        text="You chose: {} | Computer chose: {}".format(user_choice, computer))


# Create GUI window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Create labels
title_label = tk.Label(
    window, text="Rock Paper Scissors", font=("Helvetica", 20))
title_label.pack(pady=10)

choices_label = tk.Label(window, text="", font=("Helvetica", 14))
choices_label.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

# Create buttons
rock_button = tk.Button(window, text="Rock", font=(
    "Helvetica", 14), command=lambda: play_game("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", font=(
    "Helvetica", 14), command=lambda: play_game("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", font=(
    "Helvetica", 14), command=lambda: play_game("scissors"))
scissors_button.pack(pady=5)

# Run GUI window
window.mainloop()
