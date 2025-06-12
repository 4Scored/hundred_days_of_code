from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quiz_UI:
    def __init__(self, quiz_brain: QuizBrain): 
        self.q_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 20))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.q_text = self.canvas.create_text(150, 125, width=280, text="Question Text Here.", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        true_img = PhotoImage(file="images/true.png")        
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.selected_true)
        self.true_button.grid(row=2, column=1)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.selected_false)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.q_brain.still_has_questions():            
            self.score_label.config(text=f"Score: {self.q_brain.score}")
            q_text = self.q_brain.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="Quiz Finished.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def selected_true(self):                
        self.feedback(self.q_brain.check_answer("True"))

    def selected_false(self):
        self.feedback(self.q_brain.check_answer("False"))

    def feedback(self, is_right):        
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


        



