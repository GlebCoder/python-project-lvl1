#!usr/bin/env python
import prompt


NUM_Q = 3  # Number of questions in brain-games


def print_goodbye_option(user_answer, right_answer):
    print(f"'{user_answer}' is wrong answer ;(.", end=" ")
    print(f"Correct answer was '{right_answer}'")


def run_game(game_condition, question_and_answer, goodbye_opt=0):
    print("Welcome to the Brain games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print(game_condition)
    for index in range(NUM_Q):
        question, right_answer = question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer.lower():
            print('Correct!')
        elif goodbye_opt == 1:
            print_goodbye_option(user_answer, right_answer)
            return print(f"Let's try again, {name}!")
        else:
            return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")
