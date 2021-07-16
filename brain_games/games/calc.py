#!usr/bin/env python
from random import randint
import operator
import random


GAME_CONDITION = "What is the result of the expression?"
START_OF_RANGE = 1
END_OF_RANGE = 100


def generate_question_and_answer():
    num1 = randint(START_OF_RANGE, END_OF_RANGE)
    num2 = randint(START_OF_RANGE, END_OF_RANGE)
    op_dict = {'+': operator.add,
               '-': operator.sub,
               '*': operator.mul}
    op = random.choice(list(op_dict.keys()))
    question = f'{num1} {op} {num2}'
    answer = str(op_dict[op](num1, num2))
    return question, answer
