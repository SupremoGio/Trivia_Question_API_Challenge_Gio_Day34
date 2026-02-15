THEME_COLOR = "#375362"

from tkinter import *


class QuizzInterface:
    def __init__(self):
        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.geometry("350x500")
        self.window.config(background=THEME_COLOR)

        self.score = Label(text="Score: ", bg=THEME_COLOR, foreground="white", padx=20,pady=20)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.canvas.create_text(150, 125,text="cola", font=("Arial", 20,"italic"))


        self.canvas.grid(row=1,column=0,columnspan=2, padx=20, pady=20)



        self.right_image  = PhotoImage(file="images/true.png")
        self.wrong_image  = PhotoImage(file="images/false.png")


        self.wrong_button = Button(self.window, image=self.wrong_image, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1, pady=20, padx=20)

        self.right_button = Button(self.window, image=self.right_image, highlightthickness=0)
        self.right_button.grid(row=2, column=0, pady=20, padx=20)


        self.window.mainloop()