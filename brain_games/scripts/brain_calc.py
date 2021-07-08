#!usr/bin/env python
from brain_games import calc
from brain_games import engine_new


def main():
    engine_new.welcome()
    name = engine_new.get_name()
    engine_new.print_hi(name)
    calc.print_game_condition()
    game_questions = calc.generate_questions(engine_new.num_q)
    right_answers = calc.generate_right_answers(game_questions)
    if engine_new.general_script(game_questions, right_answers, goodbye_opt=1):
        return engine_new.user_wins(name)
    return engine_new.user_looses(name)


if __name__ == "__main__":
    main()
