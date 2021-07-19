#!usr/bin/env python
import prompt


MAX_NUN_OF_QUESTIONS = 3  # Maximal number of questions in brain-games


def run_game(game_condition, question_and_answer):
    print("Welcome to the Brain games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print(game_condition)
    for _ in range(MAX_NUN_OF_QUESTIONS):
        question, right_answer = question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer.lower():
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{right_answer}'")
            return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")
