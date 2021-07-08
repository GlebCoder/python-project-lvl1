#!usr/bin/env python
from brain_games import progression_game
from brain_games import engine_new


def main():
    engine_new.welcome()
    name = engine_new.get_name()
    engine_new.print_hi(name)
    progression_game.print_game_condition()
    game_questions = progression_game.generate_questions(engine_new.num_q)
    right_answers = progression_game.generate_right_answers(game_questions)
    if engine_new.general_script(game_questions, right_answers, goodbye_opt=1):
        return engine_new.user_wins(name)
    return engine_new.user_looses(name)


if __name__ == "__main__":
    main()
