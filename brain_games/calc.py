#!usr/bin/env python
from random import randint
import operator
import random


GAME_CONDITION = "What is the result of the expression?"


def generate_questions(number):
    questions = []
    for item in range(1, number + 1):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        op_dict = {'+': operator.add,
                   '-': operator.sub, '*': operator.mul}
        op = random.choice(list(op_dict.keys()))
        questions.append(f'{num1} {op} {num2}')
    return questions


def generate_right_answers(questions):
    right_answers = []
    for index, _ in enumerate(questions):
        for i, _ in enumerate(questions[index]):
            if questions[index][i] == '+':
                num1 = int(questions[index][:i])
                num2 = int(questions[index][i + 1:])
                result = num1 + num2
                right_answers.append(str(result))
            elif questions[index][i] == '-':
                num1 = int(questions[index][:i])
                num2 = int(questions[index][i + 1:])
                result = num1 - num2
                right_answers.append(str(result))
            elif questions[index][i] == '*':
                num1 = int(questions[index][:i])
                num2 = int(questions[index][i + 1:])
                result = num1 * num2
                right_answers.append(str(result))
    return right_answers
