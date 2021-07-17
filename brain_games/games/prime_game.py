#!usr/bin/env python
from random import randint


GAME_CONDITION = 'Answer "yes" if the number is prime, otherwise answer "no".'
START_OF_RANGE = 1
END_OF_RANGE = 100


def is_prime(number):
    if number > 1:
        for index in range(2, number // 2 + 1):
            if number % index != 0:
                continue
            else:
                return False
        return True
    else:
        return False


def generate_question_and_answer():
    question = randint(START_OF_RANGE, END_OF_RANGE)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
