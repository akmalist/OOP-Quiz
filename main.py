# # class
#
# class User:
#     # constructor
#     def __init__(self, user_id, username):
#         self.user_id = user_id
#         self.username = username
#         # this will be a default value that will not be required
#         # to add when we create a new class
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, person):
#         person.followers += 1
#         self.following += 1
#
#
# # object user_1 is the instance of class User
# user_1 = User("0001", "Akmalist")
#
# user_2 = User("0002", "angela")
#
# user_1.follow(user_2)
#
# print(user_1.following)
# print(user_1.followers)
#
# print(user_2.following)
# print(user_2.followers)


from data import question_data

from question_model import Question

from quiz_brain import QuizBrain


question_bank = []


for item in question_data:
    new_question = Question(item['text'], item['answer'])
    question_bank.append(new_question)

print(len(question_bank))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.points}/{quiz.question_number}")