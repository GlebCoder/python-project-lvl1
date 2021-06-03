#!usr/bin/env python
import prompt
from random import randint


def prime_game():
  # Hello and addressing the person by their name
  print("Welcome to the Brain Games!")
  name = prompt.string("May I have your name? ")
  print("Hello, {}".format(name))
  print('Answrer "yes" if a given number is prime. Otherwise answer "no".')
  # we have to ask no more than 3 times
  index = 1
  while index <= 3:
    number = randint(1, 100)
    #Finding whether this number is prime. Any prime number can be represented
    # 6n+1 or 6n-1 if it is not 2 or 3
    if number == 2 or number == 3:
        result = "yes"
    elif ((number + 1) % 6) == 0 or ((number - 1) % 6) == 0 and number != 1:
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

