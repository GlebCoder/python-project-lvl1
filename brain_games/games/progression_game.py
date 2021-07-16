#!usr/bin/env python
import random
from random import randint


GAME_CONDITION = "What number is missing in the progression?"
START_OF_RANGE_d = 1
END_OF_RANGE_d = 10
START_OF_RANGE__n = 5
END_OF_RANGE_n = 10
START_OF_RANGE_a0 = 1
END_OF_RANGE_a0 = 10


def generate_progression_list():
    d = randint(START_OF_RANGE_d, END_OF_RANGE_d)
    n = randint(START_OF_RANGE__n, END_OF_RANGE_n)
    a0 = randint(START_OF_RANGE_a0, END_OF_RANGE_a0)
    progression_list = []
    for index in range(n):
        progression_list.append(str(a0 + d * index))
    return progression_list


def generate_question_and_answer():
    progression_list = generate_progression_list()
    missing_member = random.choice(progression_list)
    for index, items in enumerate(progression_list):
        if items == missing_member:
            progression_list[index] = '..'
    question = ' '.join(progression_list)
    answer = str(missing_member)
    return question, answer
