#!usr/bin/env python
from random import randint

from brain_games import engine_new


def print_game_condition():
    part1 = 'Answer "yes" if the number is prime, '
    part2 = 'otherwise answer "no".'
    return print(part1 + part2)


def is_prime(number):
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_questions(number):
    questions = []
    for item in range(1, number + 1):
        questions.append(randint(1, 100))
    return questions


def generate_right_answers(questions):
    right_answers = []
    for item in questions:
        if is_prime(item):
            right_answers.append('yes')
            continue
        right_answers.append('no')
    return right_answers


def run_game():
    engine_new.welcome()
    name = engine_new.get_name()
    engine_new.print_hi(name)
    print_game_condition()
    game_questions = generate_questions(engine_new.num_q)
    right_answers = generate_right_answers(game_questions)
    if engine_new.general_script(game_questions, right_answers):
        return engine_new.user_wins(name)
    return engine_new.user_looses(name)
