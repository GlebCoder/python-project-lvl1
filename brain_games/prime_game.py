#!usr/bin/env python
from random import randint


GAME_CONDITION = 'Answer "yes" if the number is prime, otherwise answer "no".'


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
