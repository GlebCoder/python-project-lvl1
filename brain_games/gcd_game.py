#!usr/bin/env python
import prompt

from brain_games import engine


def gcd_game():
    game_name = 'brain-gcd'
    engine.welcome()
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    engine.game_condition(game_name)
    engine.questions_gcd(game_name, name)
