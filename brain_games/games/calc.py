#!usr/bin/env python
from random import randint
import operator
import random


GAME_CONDITION = "What is the result of the expression?"
MIN_VAL = 1
MAX_VAL = 100


def generate_question_and_answer():
    num1 = randint(MIN_VAL, MAX_VAL)
    num2 = randint(MIN_VAL, MAX_VAL)
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul}
    random_operator = random.choice(list(operators.keys()))
    question = f'{num1} {random_operator} {num2}'
    answer = str(operators[random_operator](num1, num2))
    return question, answer
