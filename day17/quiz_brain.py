from question_model import Question
from typing import List

class QuizBrain():
    def __init__(self, questions: List[Question]) -> None:
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}(True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")

        print(f"The correct answer was: {correct_answer}\nYour current score is: {self.score}/{self.question_number}\n")