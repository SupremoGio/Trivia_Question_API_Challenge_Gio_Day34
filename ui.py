THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window =  Tk()
        self.window.title("Quizzler by Gio")

        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, foreground="white", padx=20,pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,width=280,text="cola", font=("Arial", 20,"italic"))


        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)



        self.right_image  = PhotoImage(file="images/true.png")
        self.wrong_image  = PhotoImage(file="images/false.png")




        self.wrong_button = Button(self.window, image=self.wrong_image, highlightthickness=0, command=self.false_button)
        self.wrong_button.grid(row=2, column=1, pady=20, padx=20)

        self.right_button = Button(self.window, image=self.right_image, highlightthickness=0,command=self.true_button)
        self.right_button.grid(row=2, column=0, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)


    def true_button(self) :
        self.give_feedback(self.quiz.check_answer("True"))




    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

#definir bien para que regrese al color blanco
    def give_feedback(self, is_right):

        if is_right:
            self.canvas.after(100,self.canvas.config(bg="green"))
        else:
            self.canvas.config(bg="red")
        self.after_id = self.window.after(1000, self.get_next_question)

        # self.window.after_cancel(self.after_id)










