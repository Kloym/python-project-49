import random
import math

game_quest = "Find the greatest common divisor of given numbers."


def question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    answer = math.gcd(number1, number2)
    return question, answer
