class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.q_list)
    
    def next_question(self):
        current = self.q_list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current.text}. (True/False)?: ")
        self.check_answer(user_answer, current.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.title() == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"Correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.number}.")