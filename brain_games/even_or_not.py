import prompt

from brain_games import engine


def even_or_not():
    game_name = "brain-even"
    engine.welcome()  # General welcome for all the games
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    # Specicfic question for this particular game
    engine.game_condition(game_name)
    engine.questions_even(game_name, name)
