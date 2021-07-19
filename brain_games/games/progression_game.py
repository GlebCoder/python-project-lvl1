#!usr/bin/env python
import random
from random import randint


GAME_CONDITION = "What number is missing in the progression?"
MIN_COMMON_DIFF = 1
MAX_COMMON_DIFF = 10
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
MIN_FIRST_MEMBER = 1
MAX_FIRST_MEMBER = 10


def generate_progression():
    common_diff = randint(MIN_COMMON_DIFF, MAX_COMMON_DIFF)
    length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    first_member = randint(MIN_FIRST_MEMBER, MAX_FIRST_MEMBER)
    progression = []
    for i in range(length):
        progression.append(str(first_member + common_diff * i))
    return progression


def generate_question_and_answer():
    progression = generate_progression()
    random_index = random.choice(range(len(progression)))
    missing_member = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    answer = str(missing_member)
    return question, answer
