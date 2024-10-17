import random


game_quest = "What is the result of the expression?"


def question_and_answer():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operators = "+-*"
    operation = random.choice(operators)
    question = f'{number1} {operation} {number2}'
    if operation == "+":
        answer = number1 + number2
    elif operation == "-":
        answer = number1 - number2
    else:
        answer = number1 * number2
    return question, answer
