#!usr/bin/env python
from random import randint


GAME_CONDITION = "Find the greatest common divisor of given numbers"
MIN_VAL = 1
MAX_VAL = 100


def find_gcd(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 == num2:
        return num1
    if num1 > num2:
        return find_gcd(num2, num1 - num2)
    return find_gcd(num1, num2 - num1)


def generate_question_and_answer():
    num1 = randint(MIN_VAL, MAX_VAL)
    num2 = randint(MIN_VAL, MAX_VAL)
    question = f'{num1} {num2}'
    answer = str(find_gcd(num1, num2))
    return question, answer
