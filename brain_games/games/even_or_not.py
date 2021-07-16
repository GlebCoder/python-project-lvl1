from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'
START_OF_RANGE = 1
END_OF_RANGE = 100


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def generate_question_and_answer():
    question = randint(START_OF_RANGE, END_OF_RANGE)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def generate_questions():
    question = randint(1, 100)
    return question


def generate_right_answers(questions):
    right_answer = ''
    if is_even(questions):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
