import prompt
from random import randint


def even_or_not():
    print("Welcome to the Brain games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        value = randint(1, 100)
        print('Question: {}'.format(value))
        answer = prompt.string("Your answer: ")
        if (value % 2 == 0 and answer.lower() == "no") or (value % 2 == 1 and answer.lower() == "yes"):
            return print("Let's try again, {}!".format(name))
        else:
            print("Correct!")
            i += 1
    return print("Congratulations, {}!".format(name))
