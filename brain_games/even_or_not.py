from random import randint


def print_game_condition():
    part1 = 'Answer "yes" if the number is even, '
    part2 = 'otherwise answer "no".'
    return print(part1 + part2)


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def generate_questions(number):
    questions = []
    for item in range(1, number + 1):
        questions.append(randint(1, 100))
    return questions


def generate_right_answers(questions):
    right_answers = []
    for item in questions:
        if is_even(item):
            right_answers.append('yes')
            continue
        right_answers.append('no')
    return right_answers


def user_looses(name):
    return print(f"Let's try again, {name}!")
