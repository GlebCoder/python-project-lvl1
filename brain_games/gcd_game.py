#!usr/bin/env python
import math
import prompt
from random import randint


def gcd_game():
    # Hello and addressing the person by their name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    print("Find the greatest common divisor of given numbers")
    # we have to ask no more than 3 times
    # and finish the game if the answer is wrong
    # or 3 right answers are given
    index = 1
    while index <= 3:

        # Determining the question
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        question = "Question: {} {}".format(number1, number2)
        result = math.gcd(number1, number2)
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
