from tkinter import *
from random import choice

# Create main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="#4dcf25")

# Score labels
player_score = Label(root, text="0", font=("arial", 40, "bold"), bg="#9b59b6", fg="white")
computer_score = Label(root, text="0", font=("arial", 40, "bold"), bg="#9b59b6", fg="white")
player_score.grid(row=1, column=3)
computer_score.grid(row=1, column=1)

# Labels for user and computer
Label(root, text="USER", font=("arial", 15, "bold"), bg="#4dcf25", fg="black").grid(row=0, column=3)
Label(root, text="COMPUTER", font=("arial", 15, "bold"), bg="#4dcf25", fg="black").grid(row=0, column=1)

# Message Label
msg = Label(root, text="", font=("arial", 20, "bold"), bg="#4dcf25", fg="red")
msg.grid(row=3, column=2)

# Update message
def update_message(text):
    msg.config(text=text)

# Update score
def update_score(winner):
    if winner == "user":
        player_score.config(text=str(int(player_score["text"]) + 1))
    elif winner == "computer":
        computer_score.config(text=str(int(computer_score["text"]) + 1))

# Check winner
def check_winner(user_choice):
    comp_choice = choice(["rock", "paper", "scissor"])
    
    if user_choice == comp_choice:
        update_message("It's a Tie!")
    elif (user_choice == "rock" and comp_choice == "scissor") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissor" and comp_choice == "paper"):
        update_message("You Win!")
        update_score("user")
    else:
        update_message("You Lose!")
        update_score("computer")

# Reset game
def reset_game():
    player_score.config(text="0")
    computer_score.config(text="0")
    msg.config(text="")

# Buttons
Button(root, text="ROCK", width=15, command=lambda: check_winner("rock")).grid(row=2, column=1)
Button(root, text="PAPER", width=15, command=lambda: check_winner("paper")).grid(row=2, column=2)
Button(root, text="SCISSOR", width=15, command=lambda: check_winner("scissor")).grid(row=2, column=3)
Button(root, text="RESET", width=15, bg="red", fg="white", command=reset_game).grid(row=4, column=2)

root.mainloop()
