#!usr/bin/env python
from random import randint


GAME_CONDITION = 'Answer "yes" if the number is prime, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_prime(number):
    if number > 1:
        for index in range(2, number // 2 + 1):
            if number % index == 0:
                return False
        return True
    else:
        return False


def generate_question_and_answer():
    question = randint(MIN_NUM, MAX_NUM)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
