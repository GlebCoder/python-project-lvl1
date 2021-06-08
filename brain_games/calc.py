#!usr/bin/env python
import prompt
from random import randint


def calc():
    # Hello and addressing the person by their name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    print("What is the result of the expression?")
    # we have to ask no more than 3 times
    # and finish the game if the answer is wrong
    # or 3 right answers are given
    index = 1
    while index <= 3:

        # Determining the question
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        check_point = (number1 + number2) % 3
        if check_point == 0:
            result = number1 + number2
            question = f"Question: {str(number1)} + {str(number2)}"
        elif check_point == 1:
            result = number1 - number2
            question = f"Question: {str(number1)} - {str(number2)}"
        else:
            result = number1 * number2
            question = f"Question: {str(number1)} * {str(number2)}"
        # Comparing a user answer with the right result and saying goodbuy
        print(question)
        user_answer = prompt.string("Your answer: ")
        if int(user_answer) == result:
            print("Correct!")
            index += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{str(result)}'")
            return print("Let's try again, {}!".format(name))
    return print("Congratulations, {}!".format(name))
