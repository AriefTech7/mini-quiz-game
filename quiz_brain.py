class Brain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.question_list = questions_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        
    # def still_has_question2(self):
    #     on = True
    #     if not self.question_list:
    #         on = False
    #     else:
    #         while on:
    #             self.question_number += 1
    #             try:
    #                 current_question = self.question_list[self.question_number]
    #             except:
    #                 print("the question is finished")
    #                 break
    #             next_question = input(f"Q.{self.question_number}:{current_question.text} (True/False) ").capitalize()


    def nextquestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False): ").capitalize()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it answer")
            self.score += 1

        else:       
            print("you wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}\n")
        


    