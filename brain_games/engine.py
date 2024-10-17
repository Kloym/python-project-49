import prompt
from brain_games.cli import welcome_user


def run_game(game):
    name = welcome_user()
    count = 0
    while count < 3:
        question, answer = game.question_and_answer()
        print(game.game_quest)
        print(f"Question: {question}")
        user_input = prompt.string("Your answer: ")
        if user_input.lower() != str(answer):
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let`s try again, {name}!")
            break
        else:
            print("Correct!")
            count += 1
    else:
        print(f"Congratulations, {name}!")
