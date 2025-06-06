from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_q = Question(question["question"], question["correct_answer"])    
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Quiz Completed. Your final score is {quiz.score}/{quiz.question_number}")

