from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.window.title("Quiz")

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12))
        self.score_label.grid(row=0, column=1)

        self.question_area = Canvas(bg="white", width=300, height=250, highlightthickness=0, bd=0)
        self.question_text = self.question_area.create_text(150, 125, font=FONT, fill=THEME_COLOR, width=280)
        self.question_area.grid(column=0, row=1, columnspan=2, pady=50)

        correct_button_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_button_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.check_correct, bd=0)
        self.correct_button.grid(column=0, row=2, pady=20)

        wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightbackground=THEME_COLOR, highlightthickness=0, command=self.check_wrong, bd=0)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop() 

    def get_next_question(self):
        self.question_area.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.button_change_state('enable')

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_area.itemconfig(self.question_text, text=q_text)
        else:
            self.question_area.itemconfig(self.question_text, text="You've reached the of the questions")
            self.button_change_state('disable')

    def check_correct(self):
        self.button_change_state("disable")
        self.give_feedback(self.quiz.check_answer("true"))

    def check_wrong(self):
        self.button_change_state("disable")
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.question_area.config(bg="green")
        else:
            self.question_area.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def button_change_state(self, state: str):
        if state == "disable":
            self.wrong_button.config(state='disabled')
            self.correct_button.config(state='disabled')
        else:
            self.wrong_button.config(state='active')
            self.correct_button.config(state='active')

