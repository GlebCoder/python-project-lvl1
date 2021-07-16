#!usr/bin/env python
from random import randint


GAME_CONDITION = "Find the greatest common divisor of given numbers"
START_OF_RANGE = 1
END_OF_RANGE = 100


def find_gcd(num1, num2):
    max_num = max(num1, num2)
    divisors = []
    for index in range(1, max_num // 2 + 1):
        if num1 % index == 0 and num2 % index == 0:
            divisors.append(index)
    return max(divisors)


def generate_question_and_answer():
    num1 = randint(START_OF_RANGE, END_OF_RANGE)
    num2 = randint(START_OF_RANGE, END_OF_RANGE)
    question = f'{num1} {num2}'
    answer = str(find_gcd(num1, num2))
    return question, answer
