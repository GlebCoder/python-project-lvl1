#!usr/bin/env python
from brain_games.games import even_or_not
from brain_games import engine


def main():
    engine.run_game(even_or_not)


if __name__ == "__main__":
    main()
