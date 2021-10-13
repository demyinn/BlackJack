import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def hit():
    print("hit was pressed")

def stand():
    print("stand was pressed")

def new_hand():
    print("new hand was pressed")

'''
Creates the window
'''
window = tk.Tk()

window.title("Black Jack")
window.geometry("800x600")
window.configure(bg="#0C8702")

'''
Pulls one image and displays it to the screen
    - Will need to fix and update
'''
# image1 = ImageTk.PhotoImage(Image.open("PNG/2C.png"), size="10x10")
# panel1 = tk.Label(window, image=image1)
# panel1.pack(side="left")

player_frame = tk.Frame(window, bg="#0C8702")
player_frame.pack(side="top", fill="both", expand=1)

'''
First card image
'''
image1 = Image.open("PNG/2C.png")
resize_img1 = image1.resize((80, 120))
real_img = ImageTk.PhotoImage(resize_img1)
panel1 = tk.Label(player_frame, image=real_img)
panel1.image = real_img
panel1.pack(side="left")

'''
Second card image
'''
image2 = Image.open("PNG/2D.png")
resize_img2 = image2.resize((80, 120))
real_img2 = ImageTk.PhotoImage(resize_img2)
panel2 = tk.Label(player_frame, image=real_img2)
panel2.image = real_img2
panel2.pack(side="left")
'''
Creates the bottom buttons
    - Hit
    - Stand
    - New Hand
    - Quit
'''
buttons = ttk.Frame(window, padding=(20,10,20,0))
buttons.pack(side="bottom", fill="x")

hit_button = ttk.Button(buttons, text="Hit", command=hit)
hit_button.pack(side="left")
# hit_button.place(x=0, y=575)

stand_button = ttk.Button(buttons, text="Stand", command=stand)
stand_button.pack(side="left")
# stand_button.place(x=100, y=575)
# hit_button.pack(side="left")

deal_new_hand_button = ttk.Button(buttons, text="New Hand", command=new_hand)
deal_new_hand_button.pack(side="left")

quit_button = ttk.Button(buttons, text="Quit", command=window.destroy)
quit_button.pack(side="left")

window.mainloop()

