import tkinter as tk
from PIL import Image, ImageTk
import random
from playsound import playsound


# Game logic
def check(comp, user):
    if (comp == "Snake" and user == "Water") or (comp == "Water" and user == "Gun") or (comp == "Gun" and user == "Snake"):
        return "You lose"
    elif (user == "Snake" and comp == "Water") or (user == "Water" and comp == "Gun") or (user == "Gun" and comp == "Snake"):
        return "You win"
    else:
        return "It's a tie"

def play(user_choice):
    global wins, losses, ties, current_round

    if current_round == total_rounds:
        return
    
    playsound("click.mp3", block=False)

    computer_choice = random.choice(["Snake", "Water", "Gun"])
    result = check(computer_choice, user_choice)

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    if result == "You win":
        wins += 1
    elif result == "You lose":
        losses += 1
    else:
        ties += 1

    current_round += 1
    round_label.config(text=f"Round: {current_round} / {total_rounds}")
    score_label.config(text=f"Wins: {wins} | Losses: {losses} | Ties: {ties}")

    if current_round == total_rounds:
        if wins > losses:
            final_result = "\n🎉 You Won the Game!"
            result_label.config(fg="green")
            playsound("win.mp3")
        elif wins < losses:
            final_result = "\n😢 You Lost the Game!"
            result_label.config(fg="red")
            playsound("lose.mp3")
        else:
            final_result = "\n🤝 It's a Tie Game!"
            result_label.config(fg="orange")
            playsound("tie.mp3")

        result_label.config(text=f"Game Over!{final_result}")
        disable_buttons()


def reset_game():
    global wins, losses, ties, current_round
    wins = losses = ties = 0
    current_round = 0
    score_label.config(text="Wins: 0 | Losses: 0 | Ties: 0")
    round_label.config(text=f"Round: {current_round} / {total_rounds}")
    result_label.config(text="", fg="blue")
    enable_buttons()

def disable_buttons():
    snake_button.config(state='disabled')
    water_button.config(state='disabled')
    gun_button.config(state='disabled')

def enable_buttons():
    snake_button.config(state='normal')
    water_button.config(state='normal')
    gun_button.config(state='normal')

wins = losses = ties = 0
current_round = 0
total_rounds = 5  

# GUI setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("500x400")
root.config(bg="#230698")

tk.Label(root, text="Snake 🐍  Water 💧  Gun 🔫", font=("Helvetica", 16, "bold"), bg="#00DCE3", borderwidth=10).pack(pady=10)
tk.Label(root, text="Choose one:", font=("Helvetica", 12), bg="#230698").pack()

# Images
images = {}
button_icons = {}
for item in ["Snake", "Water", "Gun"]:
    img = Image.open(f"{item.lower()}.png")
    images[item] = ImageTk.PhotoImage(img)
    icon = img.resize((30, 30)) 
    button_icons[item] = ImageTk.PhotoImage(icon)

# Buttons
button_frame = tk.Frame(root, bg="#230698")
button_frame.pack(pady=10)

button_style = {
    "font": ("Arial", 12, "bold"),
    "width": 100,
    "height": 60,
    "bg": "#FFD700",
    "fg": "black",
    "compound": "left",
    "padx": 10,
    "pady": 5,
}

snake_button = tk.Button(button_frame, text="Snake", image=button_icons["Snake"],command=lambda: play("Snake"), **button_style)
snake_button.grid(row=0, column=0, padx=10)

water_button = tk.Button(button_frame, text="Water", image=button_icons["Water"],command=lambda: play("Water"), **button_style)
water_button.grid(row=0, column=1, padx=10)

gun_button = tk.Button(button_frame, text="Gun", image=button_icons["Gun"],command=lambda: play("Gun"), **button_style)
gun_button.grid(row=0, column=2, padx=10)

round_label = tk.Label(root, text=f"Round: 0 / {total_rounds}", font=("Arial", 12, "bold"), bg="#230698", fg="white")
round_label.pack(pady=5)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0", fg="blue")
result_label.pack(fill='x', pady=20)

# Score display
score_label = tk.Label(root, text="Wins: 0 | Losses: 0 | Ties: 0", font=("Arial", 12, "bold"), bg="#f0f0f0")
score_label.pack()

bottom_button_frame = tk.Frame(root, bg="#230698")
bottom_button_frame.pack(pady=15, fill="x", padx=40)

tk.Button(bottom_button_frame, text="🔁 Reset Game", font=("Arial", 12, "bold"),
          bg="#15c50b", command=reset_game).pack(side="left")

tk.Button(bottom_button_frame, text="❌ Exit Game", font=("Arial", 12, "bold"),
          bg="#db0e0e", fg="white", command=root.destroy).pack(side="right")

root.mainloop()
