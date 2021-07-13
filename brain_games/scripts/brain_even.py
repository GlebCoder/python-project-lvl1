#!usr/bin/env python
from brain_games import even_or_not
from brain_games import engine_new


def main():
    GAME_CONDITION = even_or_not.GAME_CONDITION
    game_questions = even_or_not.generate_questions(engine_new.num_q)
    right_answers = even_or_not.generate_right_answers(game_questions)
    engine_new.run_game(GAME_CONDITION, game_questions, right_answers)


if __name__ == "__main__":
    main()
