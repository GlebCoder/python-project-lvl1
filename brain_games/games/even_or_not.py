from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VAL = 1
MAX_VAL = 100


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    question = randint(MIN_VAL, MAX_VAL)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
