from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(question_description["question"], question_description["correct_answer"]) for question_description in question_data["results"]]

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
