import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Choices
choices = ["rock", "paper", "scissors"]

# Main logic
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    user_label.config(text=f"You choose: {user_choice.capitalize()}")
    comp_label.config(text=f"Computer choose: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!", fg="blue")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_score += 1
        result_label.config(text="You Win!", fg="green")
    else:
        computer_score += 1
        result_label.config(text="You lose", fg="red")

    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")
root.config(bg="#f6f1f1")

tk.Label(root, text="Rock - Paper - Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

user_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
user_label.pack()

comp_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 14), bg="#f0f0f0")
score_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("rock"))
paper_btn = tk.Button(btn_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("paper"))
scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play("scissors"))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

# Exit button
exit_btn = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="red", fg="white")
exit_btn.pack(pady=10)

root.mainloop()
