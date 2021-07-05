#!usr/bin/env python
import prompt

from brain_games import engine


def progression_game():
    game_name = "brain-progression"
    engine.welcome()  # General welcome for all the games
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    # Specicfic question for this particular game
    engine.game_condition(game_name)
    engine.questions_progression(game_name, name)
