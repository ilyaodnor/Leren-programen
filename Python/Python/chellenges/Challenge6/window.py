import tkinter as tk
from PIL import Image, ImageTk
from script import*

root = tk.Tk()
root.title('DuckHunt')

screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

root.attributes('-fullscreen', True)
photo = tk.PhotoImage(file='Python/Python/chellenges/Challenge6/assets/icon.png')
root.iconphoto(False, photo)

background_image = Image.open('Python/Python/chellenges/Challenge6/assets/stage.png')
background_photo = ImageTk.PhotoImage(background_image)
gif_image = Image.open('Python/Python/chellenges/Challenge6/assets/duck.gif')
duck_gif = ImageTk.PhotoImage(gif_image)

canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)




root.mainloop()
