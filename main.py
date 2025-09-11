# from data import question_data
from question_model import Question
from quiz_brain import Brain
from  data2 import  question_dataa

question_bank = []

for question in question_dataa:
    question_text =  question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[1].text)
# print(question_bank) # output = <question_model.Question object at 0x000001EEE9176F90>
# print(question_bank[1].answer)

brain = Brain(question_bank)
# brain adalah instance
# instance adalah object yang berdasarkan kelas 
while brain.still_has_question():
    brain.nextquestion()

print("You've completed the quiz")
print(f"Your final score was: {brain.score}/{brain.question_number}")



