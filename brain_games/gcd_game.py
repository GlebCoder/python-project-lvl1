#!usr/bin/env python
from random import randint
import math

from brain_games import engine_new


def print_game_condition():
    return print("Find the greatest common divisor of given numbers")


def generate_questions(number):
    questions = []
    for item in range(1, number + 1):
        questions.append(f'{randint(1, 100)} {randint(1, 100)}')
    return questions


def generate_right_answers(questions):
    right_answers = []
    for index, item in enumerate(questions):
        for i, symbol in enumerate(questions[index]):
            if questions[index][i] == ' ':
                num1 = int(questions[index][:i])
                num2 = int(questions[index][i:])
                result = math.gcd(num1, num2)
                right_answers.append(str(result))
    return right_answers


def run_game():
    engine_new.welcome()
    name = engine_new.get_name()
    engine_new.print_hi(name)
    print_game_condition()
    game_questions = generate_questions(engine_new.num_q)
    right_answers = generate_right_answers(game_questions)
    if engine_new.general_script(game_questions, right_answers, goodbye_opt=1):
        return engine_new.user_wins(name)
    return engine_new.user_looses(name)
