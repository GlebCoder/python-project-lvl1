#!usr/bin/env python
import prompt

from brain_games import engine


def calc():
    game_name = "brain-calc"
    engine.welcome()  # General welcome for all the games
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    # Specicfic question for this particular game
    engine.game_condition(game_name)
    engine.questions_calc(game_name, name)
