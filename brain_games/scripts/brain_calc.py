#!usr/bin/env python
from brain_games.games import calc
from brain_games import engine


def main():
    engine.run_game(calc.GAME_CONDITION, calc.generate_question_and_answer)


if __name__ == "__main__":
    main()
