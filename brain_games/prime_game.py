#!usr/bin/env python
import prompt
from random import randint


def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 < n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_game():
    # Hello and addressing the person by their name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    print('Answer "yes" if a given number is prime. Otherwise answer "no".')
    # we have to ask no more than 3 times
    index = 1
    while index <= 3:
        number = randint(1, 100)
        # Finding whether this number is prime. 
        # Idea - prime numbers can be represented in a form 6n+1 or 6n-1
        if is_prime(number) == True:
            result = "yes"
        else:
            result = "no"
        
        # Determining the question  
        question = "Question: {}".format(str(number))
        # Comparing a user answer with the right result and saying goodbuy
        print(question)
        user_answer = prompt.string("Your answer: ")
        if user_answer.lower() == result:
            print("Correct!")
            index += 1
        else:
            print("Unfortunately, you have given the wrong answer.")
            return print("Let's try again, {}!".format(name))
    return print("Congratulations, {}!".format(name))
