import random

quiz = [
    {
        "question": "Which type of language is Python?",
        "options": [
            "A.Compiled language only",
            "B.High-level programming language",
            "C.Assembly language",
            "D.Machine language"
        ],
        "answer": "High-level programming language"
    },
    {
        "question": "Which of these is a mutable data type in Python?",
        "options": [
            "A.Tuple",
            "B.String",
            "C.List",
            "D.Integer"
        ],
        "answer": "List"
    },
    {
        "question": "What is the main purpose of a function?",
        "options": [
            "A.To store only numbers",
            "B.To repeat or organize a specific piece of logic",
            "C.To create a Python file",
            "D.To delete variables"
        ],
        "answer": "To repeat or organize a specific piece of logic"
    },
    {
        "question": "Which data structure stores data as key-value pairs?",
        "options": [
            "A.List",
            "B.Tuple",
            "C.Set",
            "D.Dictionary"
        ],
        "answer": "Dictionary"
    },
    {
        "question": "What does None generally represent in Python?",
        "options": [
            "A.Zero",
            "B.An empty string",
            "C.The absence of a value",
            "D.False only"
        ],
        "answer": "The absence of a value"
    },
    {
        "question": "What is the purpose of a class in Python?",
        "options": [
            "A.To define a blueprint for creating objects",
            "B.To import libraries",
            "C.To handle errors only",
            "D.To store only strings"
        ],
        "answer": "To define a blueprint for creating objects"
    },
    {
        "question": "Which statement about tuples is correct?",
        "options": [
            "A.Tuples are mutable",
            "B.Tuples cannot contain different data types",
            "C.Tuples are immutable",
            "D.Tuples can only contain numbers"
        ],
        "answer": "Tuples are immutable"
    },
    {
        "question": "What is exception handling primarily used for?",
        "options": [
            "A.Making programs run faster",
            "B.Handling errors that occur during program execution",
            "C.Creating classes",
            "D.Converting Python into C++"
        ],
        "answer": "Handling errors that occur during program execution"
    },
    {
        "question": "What does inheritance allow in object-oriented programming?",
        "options": [
            "A.A class to receive attributes and methods from another class",
            "B.A program to run without Python",
            "C.A variable to contain only one value",
            "D.A function to execute automatically"
        ],
        "answer": "A class to receive attributes and methods from another class"
    },
    {
        "question": "Which statement best describes a module in Python?",
        "options": [
            "A.A type of loop",
            "B.A file containing Python code that can be imported and reused",
            "C.A special type of variable",
            "D.A type of exception"
        ],
        "answer": "A file containing Python code that can be imported and reused"
    }
]

random.shuffle(quiz)

score = 0

for question in quiz:
    print('\n', question.get('question'))

    options = question.get('options')
    answer = question.get('answer')

    for values in options:
        print(values)

    cleaned_values = [s[2:] for s in options]


    while True:
        user_choice = input("Enter your answer: ").upper()


        if user_choice == 'A':
            selected_option = cleaned_values[0]
        elif user_choice == 'B':
            selected_option = cleaned_values[1]
        elif user_choice == 'C':
            selected_option = cleaned_values[2]
        elif user_choice == 'D':
            selected_option = cleaned_values[3]
        else:
            print("Invalid input")
            continue

        if selected_option == answer:
            print("Correct")
            score += 1
        else:
            print("Incorrect")

        break

percentage = (score/len(quiz))*100

print("Total score: ", score , "/" , len(quiz))
print("Percentage: ", percentage)

if score < 5:
    print("Needs improvement")
elif score < 8:
    print("Good")
else:
    print("Excellent")