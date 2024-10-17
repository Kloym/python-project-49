import random

game_quest = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():
    number = random.randint(1, 100)
    question = number
    if is_prime(number) is True:
        answer = "yes"
    else:
        answer = "no"
    return (
        question,
        answer,
    )


def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True
