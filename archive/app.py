# TIC TAC TOE

import pandas as pd
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

# Database
df = pd.read_csv('data/data.csv')
print(df.head(5))

# Global Variables
width, height = 320,568
purple = "#BC5DDE"
page = 1

# App
root = Tk()
root.title("Quizz Mitsu")
root.geometry(f"{width}x{height}")
img= ImageTk.PhotoImage(Image.open("resources/star.png"))
x = iter([i for i in range(len(df))])

def do_nothing(page):
    page = 2
    print(page)

def page_one():
    frame = Frame(root, width=width, height=height, bg=purple)
    frame.place(x = 0, y = 0)
    Label(frame, text= ".Quizz", font= ('broadway 68 bold'), fg ="white", bg= purple).place( x=50, y=56)
    Label(frame, text= "Mitsu", font= ('broadway 40 bold'), fg ="white", bg= purple).place( x=110, y=126)
    Button(frame, text="Start", font=('broadway 40 bold'), bg = "white", fg = purple ,bd=0,  highlightthickness=0, command = lambda : page_two(img)).place(x=110, y=342)


def page_two(img):
    print("Switch")
    
    frame = Frame(root, width=width, height=height, bg="white")
    frame.place(x = 0, y = 0)
    canvas = Canvas(frame, width=290, height=157, bg=purple, highlightthickness=0)
    canvas.place(x = 14,y = 15)
    canvas.create_image(0, 0,anchor=NW,image=img)
    Label(frame, text= "Topic", font= ('broadway 40 bold'), fg =purple, bg= "white").place( x=26, y=188)
    Button(frame, text="Confirm", font=('broadway 40 bold'), bg = "white", fg = purple ,bd=0,  highlightthickness=0, command=lambda : quizz(x)).place(x=75, y=442)
    Button(frame, text="Perso", width= 10, height = 5, font=('broadway 10 bold'), bg = "white", fg = "black" ,bd=0,  highlightthickness=0, command=do_nothing).place(x=6, y=250)
    Button(frame, text="Pro", width= 10, height = 5, font=('broadway 10 bold'), bg = "white", fg = "black" ,bd=0,  highlightthickness=0, command=do_nothing).place(x=110, y=250)
    Button(frame, text="Asso", width= 10, height = 5, font=('broadway 10 bold'), bg = "white", fg = "black" ,bd=0,  highlightthickness=0, command=do_nothing).place(x=215, y=250)
    Label(frame, text= "Choose wisely your topic", font= ('broadway 20 bold'), fg ="black", bg= "white").place( x=26, y=320)
  

def quizz(x):
    try:
        i = next(x)
        page_three(i)
    except StopIteration:
        page_four()

        

def page_four():
    frame = Frame(root, width=width, height=height, bg=purple)
    frame.place(x = 0, y = 0)
    Label(frame, text= "END", font=('broadway 40 bold'), fg="white", bg=purple, wraplength=width - 20).place(x=30, y=56)

def page_three(i):
    frame = Frame(root, width=width, height=height, bg=purple)
    frame.place(x = 0, y = 0)
    Label(frame, text=df.iloc[i, 1], font=('broadway 40 bold'), fg="white", bg=purple, wraplength=width - 20).place(x=30, y=56)
    entry = Entry(frame, fg = "black", bg = "white", font=('broadway 17 bold'), width = 20)
    entry.place(x=30, y=300)
    user_answer = entry.get()
    print(user_answer)
    Button(frame, text="Submit", font=('broadway 20 bold'), bg="white", fg=purple, bd=0, highlightthickness=0, command= lambda : quizz(x)).place(x=110, y=342)
    

#page_two(img)
#quizz(x)
page_three(1)
root.mainloop()