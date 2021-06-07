#!usr/bin/env python
import prompt
from random import randint


def progression_game():
    # Hello and addressing the person by their name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    print("What number is missing in the progression?")
    # we have to ask no more than 3 times
    # Generate an arithmetical progression
    index = 1
    while index <= 3:
        string = ""
        d = randint(1, 10)
        n = randint(5, 10)
        a0 = randint(1, 10)
        place_for_question = randint(1, n)
        i = 1
        while i <= n:
            if i != place_for_question:
                string += str(a0 + d * (i - 1)) + " "
            else:
                string += ".. "
            i += 1

        # Determining the question
        result = a0 + d * (place_for_question - 1)
        question = "Question: {}".format(string)
        # Comparing a user answer with the right result and saying goodbuy
        print(question)
        user_answer = prompt.string("Your answer: ")
        if int(user_answer) == result:
            print("Correct!")
            index += 1
        else:
            print("'" + user_answer + "'" " is wrong answer ;(. Correct answer was '" + str(result) + "'.")
            return print("Let's try again, {}!".format(name))
    return print("Congratulations, {}!".format(name))
