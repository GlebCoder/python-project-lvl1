#!usr/bin/env python
from random import randint
import math


GAME_CONDITION = "Find the greatest common divisor of given numbers"


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
