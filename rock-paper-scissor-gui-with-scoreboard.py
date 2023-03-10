import random
import tkinter as tk

# Define game constants
OPTIONS = ['rock', 'paper', 'scissors']
WIN_CONDITIONS = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

# Initialize scores
player_score = 0
computer_score = 0

# Create GUI window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Define score label widgets
player_label = tk.Label(root, text="Player: 0")
player_label.grid(row=0, column=0)

computer_label = tk.Label(root, text="Computer: 0")
computer_label.grid(row=1, column=0)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0)

# Define button click functions


def play(option):
    global player_score, computer_score
    computer_choice = random.choice(OPTIONS)

    if option == computer_choice:
        result_label.config(text="Tie game!")
    elif WIN_CONDITIONS[option] == computer_choice:
        result_label.config(text="Player wins!")
        player_score += 1
        player_label.config(text="Player: {}".format(player_score))
    else:
        result_label.config(text="Computer wins!")
        computer_score += 1
        computer_label.config(text="Computer: {}".format(computer_score))


# Define button widgets
rock_button = tk.Button(root, text="Rock", command=lambda: play('rock'))
rock_button.grid(row=3, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play('paper'))
paper_button.grid(row=3, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors",
                            command=lambda: play('scissors'))
scissors_button.grid(row=3, column=2, padx=10, pady=10)

# Start GUI loop
root.mainloop()
