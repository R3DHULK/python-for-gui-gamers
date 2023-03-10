import tkinter as tk
import random

# Set up the GUI window
root = tk.Tk()
root.title("Football Game Simulator")

# Set up the labels and entry fields for team skill levels
label1 = tk.Label(root, text="Team 1 Skill Level:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Team 2 Skill Level:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Set up the labels for displaying the game results
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

score_label = tk.Label(root, text="")
score_label.grid(row=4, column=0, columnspan=2)

# Set up the function to simulate the game
def simulate_game():
    # Get the skill levels from the entry fields
    team1_skill = int(entry1.get())
    team2_skill = int(entry2.get())

    # Simulate the game
    team1_score = random.randint(0, team1_skill)
    team2_score = random.randint(0, team2_skill)

    # Display the results
    if team1_score > team2_score:
        result_label.config(text="Team 1 Wins!")
    elif team2_score > team1_score:
        result_label.config(text="Team 2 Wins!")
    else:
        result_label.config(text="It's a Tie!")

    score_label.config(text="Team 1: {} | Team 2: {}".format(team1_score, team2_score))

# Set up the simulate button
button = tk.Button(root, text="Simulate Game", command=simulate_game)
button.grid(row=2, column=0, columnspan=2)

# Run the GUI
root.mainloop()
