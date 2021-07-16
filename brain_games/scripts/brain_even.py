#!usr/bin/env python
from brain_games.games import even_or_not
from brain_games import engine


def main():
    GAME_CONDITION = even_or_not.GAME_CONDITION
    question_and_answer = even_or_not.generate_question_and_answer
    engine.run_game(GAME_CONDITION, question_and_answer)


if __name__ == "__main__":
    main()
