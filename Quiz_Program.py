"""
1: A dictionary that stores questions and answers
loop through the dictionary
2: A variable that tracks the scores of the player
3: loop through the dictionary using the key value pairs
4: display each question to the user and allow them to answer
5: Tell them if they're right or wrong
6: show the final result when quiz is completed
"""

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Nigeria?",
        "answer": "Abuja"
    },
    "question3": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question4": {
        "question": "Who amalgamated Nigeria?",
        "answer": "Lord Lugar"
    },
    "question5": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question6": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question7": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question8": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question9": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
    "question10": {
        "question": "What is the capital of Ethiopia",
        "answer": "Addis Ababa"
    },
    "question11": {
        "question": "What is the capital of Egypt?",
        "answer": "Cairo"
    },
    "question12": {
        "question": "What is the capital of South Africa?",
        "answer": "Pretoria"
    },
    "question13": {
        "question": "What is the capital of Ghana?",
        "answer": "Accra"
    },
    "question14": {
        "question": "What is the capital of Liberia?",
        "answer": "Moravia"
    },
    "question15": {
        "question": " The Nigeria's currency is called?",
        "answer": "The Naira"
    },
    "question16": {
        "question": "The US currency is called?",
        "answer": "USD"
    },
    "question17": {
        "question": "The UK currency is called?",
        "answer": "Uk Pounds Sterling"
    },
    "question18": {
        "question": "The Germans currency is called?",
        "answer": "the German's Dollar"
    },
    "question19": {
        "question": "The Ghana's currency is called?",
        "answer": "the cede"
    },
    "question20": {
        "question": "The Sierra-leon's currency is called?",
        "answer": "The Leon"
    },
}

score = 0
# Lets loop through the dictionary items
for key, value in quiz.items():
    # print the value of the key question
    print(value["question"])
    answer = input("Answer? ")

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score = score + 1
        # convert their score into a string
        print("Your score is: " + str(score))
        print("")
        print("")
        print("")

    else:
        print("Wrong!")
        print("The correct answer is : " + value("answer"))
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + "out of 7 questions correctly")
print("Your percentage is " + str(score/7 * 100) + "%" )