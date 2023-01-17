from data import question_data
import question_mode


from quiz_brain import QuizBrain

question_list = []

for question in question_data:

    new_q = question_mode.QuestionMode(
        question['question'], question['correct_answer'])
    question_list.append(new_q)


quizGame = QuizBrain(question_list)

while quizGame.question_limit():
    quizGame.next_question()
