#!usr/bin/env python
import prompt
from random import randint
import engine


def progression_game():
    game_name = "brain-progression"
    engine.welcome()  # General welcome for all the games
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    # Specicfic question for this particular game
    engine.game_question(game_name)
    engine.loop(game_name, name)
