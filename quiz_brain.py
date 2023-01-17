
class QuizBrain:
    def __init__(self, q_list) -> None:
        self.q_list = q_list
        self.number = 0
        self.score = 0

    def question_limit(self):
        return self.number < len(self.q_list)

    def next_question(self):
        question = self.q_list[self.number]
        self.number += 1
        user_ans = input(f"Q.{self.number}: {question.text}. (True/False): ")
        self.check_answer(user_ans, question.correct_n)

    def check_answer(self, userAns, correctAns):
        if userAns.lower() == correctAns.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correctAns}.")
        print(f"Your current score is: {self.score}/{self.number}")
