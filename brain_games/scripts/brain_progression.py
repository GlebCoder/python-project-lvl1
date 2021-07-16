#!usr/bin/env python
from brain_games.games import progression_game
from brain_games import engine


def main():
    GAME_CONDITION = progression_game.GAME_CONDITION
    question_and_answer = progression_game.generate_question_and_answer
    engine.run_game(GAME_CONDITION, question_and_answer, goodbye_opt=1)


if __name__ == "__main__":
    main()
