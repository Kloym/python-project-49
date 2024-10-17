import random

game_quest = "What number is missing in the progression?"


def question_and_answer():
    number = random.randint(1, 50)
    difference = random.randint(1, 50)
    sequence = progression(number, difference)
    random_index = random.randint(0, len(sequence) - 1)
    answer = sequence[random_index]
    sequence[random_index] = ".."
    question = " ".join(str(num) for num in sequence)
    return question, answer


def progression(number, difference):
    progression = [number]
    current_number = progression[0]
    sequence = list(progression)
    while len(sequence) < 10:
        current_number += difference
        sequence.append(current_number)
    return sequence
