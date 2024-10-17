import random


game_quest = "What is the result of the expression?"


def question_and_answer():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operators = "+-*"
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer, game_quest
