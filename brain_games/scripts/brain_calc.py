#!usr/bin/env python
from brain_games.games import calc
from brain_games import engine


def main():
    GAME_CONDITION = calc.GAME_CONDITION
    question_and_answer = calc.generate_question_and_answer
    engine.run_game(GAME_CONDITION, question_and_answer)


if __name__ == "__main__":
    main()
