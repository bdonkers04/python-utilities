"""
Author: Brandon Donkersloot
Assignment 3 - Program 4
This class models a quiz item for a quiz.
"""

class Quiz_item:
    hiddenAnswer = True
    def __init__(self, question, choices, answer): #contructor for quiz item object
        self.question = question
        self.choices = choices
        self.answer = answer

    def __str__(self): ##Retruns a readable version of the object

        return f"{self.question}{self.choices}"

    def change_question(self, question): #change question attribute
        self.question = question

    def change_choices(self, choices): #change choices attribute
        self.choices = choices

    def change_correct_answer(self, answer): #change answer attribute
        self.answer = answer

    def answer_question(self, answer): #answer the question - return true or false depending on answer
        return answer == self.answer

"""
Author: Brandon Donkersloot
Assignment 3 - Program 5
This class models a quiz item for a quiz and below is a terminal application for quiz functions. 
"""
class Quiz:

    def __init__(self, quizItems): #contructor for quiz item object
        self.quizItems = quizItems

    def __str__(self): #Retruns a readable version of the object with all attributes
        return f"{self.quizItems}"

    def add_quiz_item(self, quizItem): #add a quiz item
        self.quizItems[max(self.quizItems) +1] = quizItem

#dictionary of all quiz items to start with
allQuestions = {
    1: Quiz_item("What is the correct file extension for Python files?\n","1. .pyth \n2. .pt \n3. .py \n4. .python\n", "3"),
    2: Quiz_item("What does the print function do?\n" ,"1. print to the console \n2. print to the default printer \n3. nothing \n4. print the word print\n", "1"),
    3: Quiz_item("What is used to define a function in Python?\n","1. function \n2. def \n3. func \n4. define\n", "2")
}
#initiate quiz object
theQuiz = Quiz(allQuestions)

try:
    print("""
        Menu
        1. Add Quiz Item
        2. View all Quiz Items
        3. Modify Quiz Item
        4. Take the Quiz
        5. Exit
        """)
    decision = int(input("What would you like to do? "))
    while decision != 5:
        while decision < 1 or decision > 5:
            decision = int(input("What would you like to do? "))
        if decision == 1: #adds a quiz item
            print("You have chosen Add Quiz Item")
            newQuestion = input("Input Quiz Question ") + "\n"
            newChoice1 = input("New Choice 1") + "\n"
            newChoice2 = input("New Choice 2") + "\n"
            newChoice3 = input("New Choice 3") + "\n"
            newChoice4 = input("New Choice 4") + "\n"
            newChoices = newChoice1 + newChoice2 + newChoice3 + newChoice4 #combines all choices into one variable
            newAnswer = int(input("Input answer (int)"))
            newQuizItem = Quiz_item(newQuestion, newChoices, newAnswer) #creates new quiz item object
            theQuiz.add_quiz_item(newQuizItem) #adds new object to quiz
        elif decision == 2:
            print("You have chosen View all Quiz Items")
            for i, a in theQuiz.quizItems.items(): #prints all quiz objects and numbers
                print("Question Number ", i)
                print(a)
        elif decision == 3:
            print("You have chosen Modify Quiz Item")
            for i, a in theQuiz.quizItems.items(): #modify quiz item
                print("Question Number ", i) #quiz number - dictionary key
                print(a)#quiz question and options
            modifyQuizitem = theQuiz.quizItems[int(input("Number of question to modify"))] #picks dictionary key for quiz number
            whatToModify = input("""
            1. Question
            2. Options
            3. Answer
            What do you want to modify?
            """)
            if whatToModify == 1:
                newQuestion = input("Input new question")
                modifyQuizitem.change_question(newQuestion) #changes question of the quiz item
            elif whatToModify == 2:
                newChoice1 = input("New Choice 1") + "\n"
                newChoice2 = input("New Choice 2") + "\n"
                newChoice3 = input("New Choice 3") + "\n"
                newChoice4 = input("New Choice 4") + "\n"
                newChoices = newChoice1 + newChoice2 + newChoice3 + newChoice4 #combines all choices into one variable
                modifyQuizitem.change_choices(newChoices) #changes choice od the quiz item
            else:
                newAnswer = input("Input new answer")
                modifyQuizitem.change_correct_answer(newAnswer) #changes answer of the quiz item
        elif decision == 4:
            print("You have chosen Take the Quiz")
            for i, a in theQuiz.quizItems.items(): #prints quiz questions one at a time
                print("Question Number ", i) #quiz number - dictionary key
                print(a) #quiz question and options
                userAnswer = input("What is your answer")
                print(theQuiz.quizItems[i].answer_question(userAnswer)) #prints true or false depending on the asnwer
        else:
            print("You have chosen Exit")
            break  # exit the loop, program ends
        decision = int(input("What would you like to do? "))

except Exception as e:
    print(e)
