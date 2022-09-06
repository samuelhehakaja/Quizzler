from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Questions
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="xxx", font=("Arial", 20, "italic"), width=280,
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_check)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_check)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"QUIZ OVER\nScore: {self.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_check(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_check(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.score}")
        self.window.after(1000, self.next_question)