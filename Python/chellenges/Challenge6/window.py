import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title('DuckHunt')
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
photo = tk.PhotoImage(file='Leren-programen/Python/Python/chellenges/Challenge6/assets/icon.png')
root.iconphoto(False, photo)

background_image = Image.open('Leren-programen/Python/Python/chellenges/Challenge6/assets/stage.png')
background_photo = ImageTk.PhotoImage(background_image)

canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=background_photo)

duck_image = "Leren-programen/Python/Python/chellenges/Challenge6/assets/duck.gif"
gif = Image.open(duck_image)

frames = []
try:
    while True:
        frame = ImageTk.PhotoImage(gif.copy())
        frames.append(frame)
        gif.seek(gif.tell() + 1)
except EOFError:
    pass

current_frame = 0
gif_x, gif_y = random.randint(0, screen_width - 100), random.randint(0, screen_height - 100)
dx, dy = 5, 5

def update_frame():
    global current_frame
    canvas.delete("duck")
    canvas.create_image(gif_x, gif_y, anchor="nw", image=frames[current_frame], tags="duck")
    current_frame = (current_frame + 1) % len(frames)
    root.after(100, update_frame)

def move_duck():
    global gif_x, gif_y, dx, dy
    gif_x += dx
    gif_y += dy

    if gif_x <= 0 or gif_x >= screen_width - 100:
        dx = -dx
    if gif_y <= 0 or gif_y >= screen_height - 100:
        dy = -dy

    canvas.move("duck", dx, dy)
    root.after(50, move_duck)

def on_duck_click(event):
    global dx, dy
    dx, dy = random.choice([-5, 5]), random.choice([-5, 5])

canvas.tag_bind("duck", "<Button-1>", on_duck_click)
update_frame()
move_duck()
root.mainloop()
