import pandas as pd
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
import os

class QuizzApp(Tk):
    """
    QuizzApp class represents the main application.

    Attributes:
    - data (pd.DataFrame): DataFrame containing quiz data.
    - width (int): Width of the application window.
    - height (int): Height of the application window.
    - purple (str): Hex color code for the purple color theme.
    - img (PhotoImage): Image for Home page.
    - question_index (iterable): Iterator for the question index.
    """
    def __init__(self, width = 320, height = 568):
        Tk.__init__(self)
        self.data = pd.read_csv('data/data.csv')
        self.data['user_answer'] = "test"
        self.width = width
        self.height = height
        self.geometry(f"{width}x{height}")
        self.purple = "#BC5DDE"
        self.title("Quizz Mitsu")
        self.img= ImageTk.PhotoImage(Image.open("resources/star.png"))
        self.question_index = iter([i for i in range(len(self.data))])
        self.topic_choice = 'personal' # choose between personal, professional and association
        self.topic_data = self.data[self.data['topic'] == self.topic_choice]
        self.start()

    def start(self):
        page = Pages(self)
        page.openpage()

class Pages():
    """
    Pages class represents the different pages of the application.

    Attributes:
    - root (QuizzApp): Reference to the QuizzApp instance.
    """
    def __init__(self, root):
        self.root = root

    def openpage(self):
        """
        Create and show the StartPage.
        """
        frame = Frame(self.root, width=self.root.width, height=self.root.height, bg=self.root.purple)
        frame.place(x = 0, y = 0)
        Label(frame, text= ".Quizz", font= ('broadway 68 bold'), fg ="white", bg= self.root.purple).place( x=50, y=56)
        Label(frame, text= "Mitsu", font= ('broadway 40 bold'), fg ="white", bg= self.root.purple).place( x=110, y=126)
        Button(frame, text="Start", font=('broadway 40 bold'), bg = "white", fg = self.root.purple ,bd=0,  highlightthickness=0, command =  self.homepage).place(x=110, y=342)

    def homepage(self):
        """
        Create and show the HomePage.
        """
        frame = Frame(self.root, width=self.root.width, height=self.root.height, bg="white")
        frame.place(x = 0, y = 0)
        canvas = Canvas(frame, width=290, height=157, bg=self.root.purple, highlightthickness=0)
        canvas.place(x = 14,y = 15)
        canvas.create_image(0, 0,anchor=NW,image=self.root.img) 
        Label(frame, text= "Topic", font= ('broadway 40 bold'), fg =self.root.purple, bg= "white").place( x=26, y=188)
        Button(frame, text="Confirm", font=('broadway 40 bold'), bg = "white", fg = self.root.purple ,bd=0,  highlightthickness=0, command= self.quizz).place(x=72, y=442)
        Button(frame, text="Perso", width= 10, height = 5, font=('broadway 10 bold'), bg = "white", fg = "black" ,bd=0,  highlightthickness=0, command= lambda :self.set_topic('personal')).place(x=6, y=250)
        Button(frame, text="Pro", width= 10, height = 5, font=('broadway 10 bold'), bg = "white", fg = "black" ,bd=0,  highlightthickness=0, command=lambda : self.set_topic('professional')).place(x=110, y=250)
        Button(frame, text="Asso", width= 10, height = 5, font=('broadway 10 bold'), bg = "white", fg = "black" ,bd=0,  highlightthickness=0, command= lambda : self.set_topic('association')).place(x=215, y=250)
        Label(frame, text= "Choose wisely your topic", font= ('broadway 20 bold'), fg ="black", bg= "white").place( x=26, y=330)

    def set_topic(self, topic):
        """
        Set the topic that we want for the quiz
        """
        self.root.topic_choice = topic
        self.root.topic_data = self.root.data[self.root.data['topic'] == self.root.topic_choice]
        self.root.topic_data = self.root.topic_data.reset_index()
        self.root.topic_data = self.root.topic_data.drop("index", axis = 1)
        self.root.question_index = iter([i for i in range(len(self.root.topic_data))])
        Label(self.root, text= f"You chose the topic : {self.root.topic_choice}", font= ('broadway 15 bold'), fg ="black", bg= "white").place( x=29, y=380)


    def quizz(self, entry=None, i = None):
        """
        Start the quiz and transition to the QuizzPage.
        """
        if entry is not None:
            user_answer = entry.get()
            self.root.topic_data.loc[i, ['user_answer']] = user_answer
        try:
            i = next(self.root.question_index)
            self.question_page(i)
        except:
            self.end_page()
        
    def end_page(self):
        """
        Ending page once the quizz is over
        """
        
        frame = Frame(self.root, width=self.root.width, height=self.root.height, bg=self.root.purple)
        frame.place(x = 0, y = 0)
        self.root.score = (self.root.topic_data.iloc[:,2] == self.root.topic_data.iloc[:,3]).sum() / len(self.root.topic_data.iloc[:,2])*100
        Label(frame, text= "Game has ended", font=('broadway 40 bold'), fg="white", bg=self.root.purple, wraplength=self.root.width - 20).place(x=30, y=56)
        Label(frame, text= f"Your score {self.root.score}%", font=('broadway 40 bold'), fg="white", bg=self.root.purple, wraplength=self.root.width - 20).place(x=30, y=200)
        self.root.data.to_csv("data/output.csv")
        Button(frame, text="Quit", font=('broadway 40 bold'), bg = "white", fg = self.root.purple ,bd=0,  highlightthickness=0, command =  self.root.destroy).place(x=200, y=342)
        Button(frame, text="Home", font=('broadway 40 bold'), bg = "white", fg = self.root.purple ,bd=0,  highlightthickness=0, command =  self.homepage).place(x=15, y=342)


    def question_page(self, i):
        """
        display each question
        """
        frame = Frame(self.root, width=self.root.width, height=self.root.height, bg=self.root.purple)
        frame.place(x = 0, y = 0)
        Label(frame, text=self.root.topic_data.iloc[i, 1], font=('broadway 40 bold'), fg="white", bg=self.root.purple, wraplength=self.root.width - 40).place(x=30, y=56)
        entry = Entry(frame, fg = "black", bg = "white", font=('broadway 17 bold'), width = 20)
        entry.place(x=30, y=300)
        Button(frame, text="Submit", font=('broadway 20 bold'), bg="white", fg=self.root.purple, bd=0, highlightthickness=0, command= lambda: self.quizz(entry, i)).place(x=110, y=342)
        
if __name__ == '__main__':
    app = QuizzApp()
    app.mainloop()
