import tkinter as tk
from tkinter import ttk
import random

BTN_WIDTH, GAME_TIME = 20, 20
score, time_left, current_command, current_button = 0, GAME_TIME, None, None

commands = {
    'druk op de w': '<w>',
    'druk op de a': '<a>',
    'druk op de s': '<s>',
    'druk op de d': '<d>',
    'druk op de spatiebalk': '<space>',
    'enkele klik': '<Button-1>',
    'dubbele klik': '<Double-Button-1>',
    'drieble klik': '<Triple-Button-1>'
}

root = tk.Tk()
root.geometry('800x500')
root.title('FPS Trainer')
root.config(bg='white')


score_label = ttk.Label(root, text=f'Score: {score}', background='red', font=('Arial', 12))
score_label.pack(anchor='se')

time_label = ttk.Label(root, text=f'Time left: {time_left}', background='gray', font=('Arial', 12), width=20)
time_label.place(x=0, y=0)


def center_window(window, width, height):
   
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

window_width = 800
window_height = 500
center_window(root, window_width, window_height)

def random_command():
    return random.choice(list(commands.items()))

def button_mechanik():
    global current_command, current_button
    if current_button:
        current_button.destroy()
    current_command = random_command()
    current_button = ttk.Button(root, text=current_command[0], width=BTN_WIDTH)
    current_button.place(
        x=random.randint(0, root.winfo_width() - 150),
        y=random.randint(30, root.winfo_height() - 100)
    )
    if current_command[1] in ['<Button-1>', '<Double-Button-1>', '<Triple-Button-1>']:
        current_button.bind(current_command[1], lambda e: correct_button_pressed())

def correct_button_pressed(event=None):
    global score
    score += 1
    score_label.config(text=f'Score: {score}')
    button_mechanik()

def update_time():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text=f'Time left: {time_left}')
        root.after(1000, update_time)
    else:
        end_game()

def end_game():
    if current_button:
        current_button.destroy()
    ttk.Label(root, text=f"Игра окончена! Ваш счёт: {score}", font=('Arial', 16), background='white').pack(expand=True)

def game():
    global score, time_left
    score, time_left = 0, GAME_TIME
    score_label.config(text=f'Score: {score}')
    time_label.config(text=f'Time left: {time_left}')
    btn_start.pack_forget()
    update_time()
    button_mechanik()

def on_key_press(event):
    if current_command and current_command[1] == f'<{event.keysym}>':
        correct_button_pressed()

root.bind("<Key>", on_key_press)

btn_start = ttk.Button(root, text="Klik om te starten", width=BTN_WIDTH, command=game)
btn_start.pack(anchor='center')

root.mainloop()
