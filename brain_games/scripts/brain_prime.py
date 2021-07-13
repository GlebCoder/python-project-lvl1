#!usr/bin/env python
from brain_games import prime_game
from brain_games import engine_new


def main():
    GAME_CONDITION = prime_game.GAME_CONDITION
    game_questions = prime_game.generate_questions(engine_new.num_q)
    right_answers = prime_game.generate_right_answers(game_questions)
    engine_new.run_game(GAME_CONDITION, game_questions, right_answers)


if __name__ == "__main__":
    main()
