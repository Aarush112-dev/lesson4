from tkinter import *
from time import strftime
import random

window = Tk()
window.geometry("300x75")
window.title("digital clock")

colours = ["red","orange","yellow","blue","purple","green","pink"]
hex_colours = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

def update_time():
    current_time = strftime("%H:%M:%S %p")
    text_colour = random.choice(colours)
    bg_colour = random.choice(colours)
    first = random.choice(hex_colours)
    second = random.choice(hex_colours)
    third = random.choice(hex_colours)
    fourth = random.choice(hex_colours)
    fifth = random.choice(hex_colours)
    sixth = random.choice(hex_colours)
    bg_colour2 = "#" + "".join([random.choice("0123456789ABCDEF") for i in range(6)])

    if text_colour == bg_colour:
        text_colour = random.choice(colours)
        bg_colour = random.choice(colours)
    time.config(text=current_time,fg="#{}{}{}{}{}{}".format(first,second,third,fourth,fifth,sixth),background=bg_colour2)
    time.after(1000,update_time)
    

time = Label(window,text="",font=("times",40),background="white")
time.pack(anchor="center")

update_time()

window.mainloop()