#!usr/bin/env python
import random
import math
from random import randint
import prompt
import operator
from brain_games import is_prime


num_q = 3  # Number of questions in brain-games


def welcome():
    return print("Welcome to the Brain games!")


def game_question(game_name):
    if game_name == "brain-even":
        return print('Answer "yes" if the number is even, otherwise answer "no".')
    if game_name == "brain-calc":
        return print("What is the result of the expression?")
    if game_name == "brain-progression":
        return print("What number is missing in the progression?")
    if game_name == "brain-gcd":
        return print("Find the greatest common divisor of given numbers")
    if game_name == "brain-prime":
        return print('Answer "yes" if a given number is prime. Otherwise answer "no".')


def correct():
    print("Correct!")


def sad_bye(game_name, name, result, user_answer):
    if game_name == "brain-even":
        print(f"Let's try again, {name}")
    if game_name == "brain-prime":
        print("Unfortunately, you have given the wrong answer.")
        print(f"Let's try again, {name}")
    if game_name == "brain-calc":
        print(f"'{user_answer}' is wrong answer ;(.", end=" ")
        print(f"Correct answer was '{str(result)}'")
        print("Let's try again, {}!".format(name))
    if game_name == 'brain-gcd':
        print(f"'{user_answer}' is wrong answer ;(.", end=" ")
        print(f"Correct answer was '{str(result)}'")
        print("Let's try again, {}!".format(name))
    if game_name == 'brain-progression':
        print(f"'{user_answer}' is wrong answer ;(.", end=" ")
        print(f"Correct answer was '{str(result)}'")
        print("Let's try again, {}!".format(name))


def you_win(name):
    print(f"Congratulations, {name}")


def is_even(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def loop(game_name, name):
    for i in range(1, num_q + 1):
        if game_name == 'brain-even':
            value = randint(1, 100)
            result = is_even(value)
            print("Question: ", value)
        if game_name == 'brain-calc':
            num1 = randint(1, 100)
            num2 = randint(1, 100)
            op_dict = {'+': operator.add,
                       '-': operator.sub, '*': operator.mul}
            op = random.choice(list(op_dict.keys()))
            result = str(op_dict.get(op)(num1, num2))
            print(f'Question: {num1} {op} {num2}')
        if game_name == 'brain-gcd':
            num1 = randint(1, 100)
            num2 = randint(1, 100)
            result = str(math.gcd(num1, num2))
            print(f'Question: {num1} {num2}')
        if game_name == 'brain-prime':
            num = randint(1, 100)
            if is_prime.is_prime(num):
                result = 'yes'
            else:
                result = 'no'
            print(f'Question: {num}')
        if game_name == 'brain-progression':
            question = ""
            d = randint(1, 10)
            n = randint(5, 10)
            a0 = randint(1, 10)
            place_for_question = randint(1, n)
            i = 1
            while i <= n:
                if i != place_for_question:
                    question += str(a0 + d * (i - 1)) + " "
                else:
                    question += ".. "
                i += 1
            result = str(a0 + d * (place_for_question - 1))
            print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if result == user_answer.lower():
            correct()
        else:
            return sad_bye(game_name, name, result, user_answer)
    return you_win(name)
