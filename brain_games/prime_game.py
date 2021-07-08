#!usr/bin/env python
from random import randint


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


def user_looses(name):
    print("Unfortunately, you have given the wrong answer.")
    return print(f"Let's try again, {name}!")
