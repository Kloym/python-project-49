import random
import math

game_quest = "Find the greatest common divisor of given numbers."


def question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    answer = math.gcd(num1, num2)
    return (
        question,
        answer,
    )
