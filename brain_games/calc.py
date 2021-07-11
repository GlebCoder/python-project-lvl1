#!usr/bin/env python
from random import randint
import operator
import random

from brain_games import engine_new


def print_game_condition():
    return print("What is the result of the expression?")


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


def run_game():
    engine_new.welcome()
    name = engine_new.get_name()
    engine_new.print_hi(name)
    print_game_condition()
    game_questions = generate_questions(engine_new.num_q)
    right_answers = generate_right_answers(game_questions)
    if engine_new.general_script(game_questions, right_answers, goodbye_opt=1):
        return engine_new.user_wins(name)
    return engine_new.user_looses(name)
