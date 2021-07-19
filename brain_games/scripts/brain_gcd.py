#!usr/bin/env python
from brain_games.games import gcd_game
from brain_games import engine


def main():
    engine.run_game(gcd_game.GAME_CONDITION,
                    gcd_game.generate_question_and_answer)


if __name__ == "__main__":
    main()
