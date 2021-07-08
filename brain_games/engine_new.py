#!usr/bin/env python
import prompt


num_q = 3  # Number of questions in brain-games


def welcome():
    return print("Welcome to the Brain games!")


def get_name():
    name = prompt.string("May I have your name? ")
    return name


def print_hi(name):
    return print(f"Hello, {name}")


def correct():
    return print("Correct!")


def user_wins(name):
    return print(f"Congratulations, {name}!")


def general_script(questions, right_answers, goodbye_opt=0):
    for index, item in enumerate(questions):
        print(f"Question: {item}")
        user_answer = prompt.string("Your answer: ")
        if right_answers[index] == user_answer.lower():
            correct()
        elif goodbye_opt == 1:
            print_goodbye_option(user_answer, right_answers[index])
            return False
        else:
            return False
    return True


def print_goodbye_option(user_answer, right_answer):
    print(f"'{user_answer}' is wrong answer ;(.", end=" ")
    print(f"Correct answer was '{right_answer}'")


def user_looses(name):
    return print(f"Let's try again, {name}!")
