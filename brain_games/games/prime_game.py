#!usr/bin/env python
from random import randint


GAME_CONDITION = 'Answer "yes" if the number is prime, otherwise answer "no".'
START_OF_RANGE = 1
END_OF_RANGE = 100


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


def generate_question_and_answer():
    question = randint(START_OF_RANGE, END_OF_RANGE)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
