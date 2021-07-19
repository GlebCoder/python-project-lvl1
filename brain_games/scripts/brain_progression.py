#!usr/bin/env python
from brain_games.games import progression_game
from brain_games import engine


def main():
    engine.run_game(progression_game.GAME_CONDITION,
                    progression_game.generate_question_and_answer)


if __name__ == "__main__":
    main()
