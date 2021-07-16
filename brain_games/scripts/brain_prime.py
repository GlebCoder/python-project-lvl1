#!usr/bin/env python
from brain_games.games import prime_game
from brain_games import engine


def main():
    GAME_CONDITION = prime_game.GAME_CONDITION
    question_and_answer = prime_game.generate_question_and_answer
    engine.run_game(GAME_CONDITION, question_and_answer)


if __name__ == "__main__":
    main()
