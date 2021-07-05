#!usr/bin/env python
import math
import prompt
import engine
from random import randint


def gcd_game():
    game_name = 'brain-gcd'
    engine.welcome()
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    engine.game_question(game_name)
    engine.loop(game_name, name)
